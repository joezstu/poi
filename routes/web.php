<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
use GuzzleHttp\Client;
use Illuminate\Support\Facades\Input;
use App\Imports\PoisImport;
use Maatwebsite\Excel\Facades\Excel;
use App\Pois;


Route::prefix('api')->group(function () {
    Route::post('import', function () {

//        $pois = new Pois();
//
//        DB::table('pois')->truncate();
//
//        //上传excel
//    $file = Input::file('e_file');

//    $realPath = $file->store('temp');

        $arr = [
            [
                'name'  =>  '张三',
            ],
            [
                'name'  =>  '李四'
            ]
        ];

        return json_encode($arr);

    Excel::import(new PoisImport, storage_path('app') . '/' . $realPath);
    });


});


Route::get('/{any}',function(){
    return view('welcome', ['name' => 'James']);
})->where('any', '.*');
//
//Route::post('/export', function () {
//
//
//    //上传excel
//    $file = Input::file('e_file');
//
//    $realPath = $file->getRealPath();
//
//    $excel_data = Excel::load($realPath)->toArray();
//
//    foreach($excel_data as $kkk => $vvv){
//        if($kkk != 0){
//            $key = "5e0ead6b227ee7d038d4450e5e263ed3";
//
//            $url = "https://restapi.amap.com/v3/place/text?key=".$key."&keywords=".$vvv[22]."&extensions=all";
//
//            $client = new Client();
//
//            $response = $client->request('GET', $url);
//            $response = json_decode($response->getBody());
//            $response = $response->pois;
//
//            if(isset($response[0]) && !empty($response[0])){
//                $value = $response[0];
//
//                $url2 = "https://restapi.amap.com/v3/place/around?key=".$key."&location=".$value->location."&radius=10000&keywords=工商银行&sortrule=distance&offset=10&page=1";
//
//                $r = $client->request('GET', $url2);
//                $r = json_decode($r->getBody());
//                $r = $r->pois;
//
//                $string = '';
//
//                foreach($r as $kk => $vv){
//                    $string .= $vv->name;
//                    $string .= ",";
//                }
//
//                $excel_data[$kkk][25] = '';
//
//                if(is_string($value->pname) && !empty($value->pname)){
//                    $excel_data[$kkk][25] .= $value->pname;
//                }
//                if(is_string($value->cityname) && !empty($value->cityname)){
//                    $excel_data[$kkk][25] .= $value->cityname;
//                }
//                if(is_string($value->address) && !empty($value->address)){
//                    $excel_data[$kkk][25] .= $value->address;
//                }
//
//                $excel_data[$kkk][26] = $string;
//            }
//
//
//
//
//        }else{
//            $excel_data[$kkk][25] = "返回地址";
//            $excel_data[$kkk][26] = "返回银行";
//        }
//    }
//
//
//    //如果你要导出csv或者xlsx文件，只需将 export 方法中的参数改成csv或xlsx即可。
//    //如果还要将该Excel文件保存到服务器上，可以使用 store 方法
//    \Excel::create(iconv('UTF-8', 'GBK', '返回数据'),function($excel) use ($excel_data){
//        $excel->sheet('返回数据', function($sheet) use ($excel_data){
//            $sheet->fromArray($excel_data);
//        });
//    })->export('xls');
//
//
//
//
//
//
//    echo '<pre>';print_r($response);exit;
//});
