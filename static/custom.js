$(document).ready(function(){
    $('.btn_class').on('click', function(){
        var btn_proparty = $(this)
        var row = $(this).closest("tr");
        var roll = row.find(".cls_roll").text();
        var cls = row.find(".cls_class").text();
        
        var url = "http://127.0.0.1:8000/api/attendance/"+cls+"/"+roll;
        var api_url = url.replace(/\s/g,'')
        console.log(api_url)

        $.ajax({
            url: api_url,
            method: 'get',
            success: function(data){
                btn_proparty.addClass('btn btn-success');

                
            },
            error: function(err){
                alert(err.status)
            },
        });
    })
    
})