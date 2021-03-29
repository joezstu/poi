<?php

namespace App\Imports;

use App\Pois;
use Maatwebsite\Excel\Concerns\ToModel;

class PoisImport implements ToModel
{
    /**
    * @param array $row
    *
    * @return \Illuminate\Database\Eloquent\Model|null
    */
    public function model(array $row)
    {
        return new Pois([
            //
        ]);
    }
}
