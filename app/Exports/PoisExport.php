<?php

namespace App\Exports;

use App\Pois;
use Maatwebsite\Excel\Concerns\FromCollection;

class PoisExport implements FromCollection
{
    /**
    * @return \Illuminate\Support\Collection
    */
    public function collection()
    {
        return Pois::all();
    }
}
