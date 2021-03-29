<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Pois extends Model
{
    // 加上对应的字段
    protected $fillable = [
        'company_name',
        'registration_status',
        'boss',
        'registered_capital',
        'setup_date',
        'approval_date',
        'provinces',
        'city',
        'county',
        'telephone',
        'more_telephone',
        'email',
        'more_email',
        'credit_code',
        'taxpayers_code',
        'registered_code',
        'organization_code',
        'contributors',
        'company_type',
        'former_name',
        'website',
        'company_address',
        'new_company_address',
        'business_scope',
        ];


}
