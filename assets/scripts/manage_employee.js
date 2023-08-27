$(document).ready(function(){
    $('#add_new_emp').click(function(){
        display()
    });
    function display (){
        $('#manage_employee_update, #manage_employee_view, #manage_employee_archive').css('display, none');
        $("#manage_employee_add").css({
            'flex': 3,
            'display': 'flex'
        })

    }
});