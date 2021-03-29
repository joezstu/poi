<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class AddVotesToPoisTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('pois', function (Blueprint $table) {
            //企业名称
            $table->string('company_name')->comment('企业名称');
            //登记状态
            $table->boolean('registration_status')->comment('登记状态');
            //法定代表人
            $table->string('boss')->comment('法定代表人');
            //注册资本
            $table->double('registered_capital',8)->comment('注册资本');
            //成立日期
            $table->date('setup_date')->comment('成立日期');
            //核准日期
            $table->date('approval_date')->comment('核准日期');
            //所属省份
            $table->string('provinces')->comment('所属省份');
            //所属城市
            $table->string('city')->comment('所属城市');
            //所属区县
            $table->string('county')->comment('所属区县');
            //电话
            $table->string('telephone')->comment('电话');
            //更多电话
            $table->string('more_telephone')->comment('更多电话');
            //邮箱
            $table->string('email')->comment('邮箱');
            //更多邮箱
            $table->string('more_email')->comment('更多邮箱');
            //统一社会信用代码
            $table->string('credit_code')->comment('统一社会信用代码');
            //纳税人识别号
            $table->string('taxpayers_code')->comment('纳税人识别号');
            //注册号
            $table->string('registered_code')->comment('注册号');
            //组织机构代码
            $table->string('organization_code')->comment('组织机构代码');
            //参保人数
            $table->string('contributors')->comment('参保人数');
            //企业类型
            $table->string('company_type')->comment('企业类型');
            //所属行业
            $table->string('industry')->comment('所属行业');
            //曾用名
            $table->string('former_name')->comment('曾用名');
            //网址
            $table->string('website')->comment('网址');
            //企业地址
            $table->string('company_address')->comment('企业地址');
            //最新年报地址
            $table->string('new_company_address')->comment('最新年报地址');
            //经营范围
            $table->text('business_scope')->comment('经营范围');
            //参考地址，由于目的是寻找公司所在地址的附近10个工商银行，而且公司的地址可能不存在或者多个，因此默认选择第一个地址
            $table->string('reference_address')->comment('参考地址');
            //返回数据
            $table->text('result_data')->comment('返回数据');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('pois', function (Blueprint $table) {

        });
    }
}
