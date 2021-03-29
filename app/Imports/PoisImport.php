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
            'company_name'  =>  $row[0],
            'registration_status'  =>  $row[1],
            'boss'  =>  $row[2],
            'registered_capital'  =>  $row[3],
            'setup_date'  =>  $row[4],
            'approval_date'  =>  $row[5],
            'provinces'  =>  $row[6],
            'city'  =>  $row[7],
            'county'  =>  $row[8],
            'telephone'  =>  $row[9],
            'more_telephone'  =>  $row[10],
            'email'  =>  $row[11],
            'more_email'  =>  $row[12],
            'credit_code'  =>  $row[13],
            'taxpayers_code'  =>  $row[14],
            'registered_code'  =>  $row[15],
            'organization_code'  =>  $row[16],
            'contributors'  =>  $row[17],
            'company_type'  =>  $row[18],
            'industry'  =>  $row[19],
            'former_name'  =>  $row[20],
            'website'  =>  $row[21],
            'company_address'  =>  $row[22],
            'new_company_address'  =>  $row[23],
            'business_scope'  =>  $row[24],
            'reference_address'  =>  '',
            'result_data'  =>  '',
        ]);
    }
}
