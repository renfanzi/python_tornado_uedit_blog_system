
//$(function(){
// localStorage.setItem('sub_url', 'http://www.muyuchen.com:8888/static');
//});


function Base(){
/*
use method:
    <script type="text/javascript" src="/static/admin/js/base.js"></script>
    <script type="text/javascript">
        window.onload=function(){
            var aaaa = Base();
            console.log(aaaa["sub_url"]); //'http://www.muyuchen.com:8888/static'
        };
        =======================
        window.onload=function(){
            var aaaa = Base()["sub_url"];
            console.log(aaaa);
        };
    </script>


*/

    var data = {};
    data["sub_url"] = 'http://www.muyuchen.com:8888/static';
    return data;
};
