<?php

namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Queue\SerializesModels;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use App\Pois;
use Illuminate\Support\Facades\DB;
use GuzzleHttp\Client;

class TestJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    protected $poi = null;

    /**
     * Create a new job instance.
     *
     * @return void
     */
    public function __construct(Pois $poi)
    {
        $this->poi = $poi;
    }

    /**
     * Execute the job.
     *
     * @return void
     */
    public function handle()
    {

            $key = "5e0ead6b227ee7d038d4450e5e263ed3";

            $url = "https://restapi.amap.com/v3/place/text?key=".$key."&keywords=".$this->poi->company_address."&extensions=all";

            $client = new Client();

            $response = $client->request('GET', $url);
            $response = json_decode($response->getBody());
            if(!empty($response->pois)){
                $response = $response->pois;

                if(isset($response[0]) && !empty($response[0])){
                    $value = $response[0];

                    $url2 = "https://restapi.amap.com/v3/place/around?key=".$key."&location=".$value->location."&radius=10000&keywords=工商银行&sortrule=distance&offset=10&page=1";

                    $r = $client->request('GET', $url2);
                    $r = json_decode($r->getBody());
                    $r = $r->pois;
                    if(isset($r) && !empty($r) && is_object($r)){

                        $string = '';

                        foreach($r as $kk => $vv){
                            if(is_object($vv)){
                                $string .= $vv->name ."-" . (isset($vv->address) && is_string($vv->address) ? $vv->address : '无') . '-' . $vv->distance . '米';
                                $string .= "\n";
                            }
                        }

                        if(is_string($value->pname) && !empty($value->pname)){
                            $this->poi->reference_address .= $value->pname;
                        }
                        if(is_string($value->cityname) && !empty($value->cityname)){
                            $this->poi->reference_address .= $value->cityname;
                        }
                        if(is_string($value->address) && !empty($value->address)){
                            $this->poi->reference_address .= $value->address;
                        }

                        $this->poi->result_data = $string;
                    }
                }
            }

            $this->poi->status = 1;

            $this->poi->save();



    }



}
