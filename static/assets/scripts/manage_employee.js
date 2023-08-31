// $(document).ready(function(){
//     $('#add_new_emp').click(function(){
//         display()
//     });
//     function display (){
//         $('#manage_employee_update, #manage_employee_view, #manage_employee_archive').css('display, none');
//         $("#manage_employee_add").css({
//             'flex': 3,
//             'display': 'flex'
//         })

//     }
// });
$(document).ready(function(){
    const buttons = [
        {id: '#add_new_emp', contentId: '#manage_employee_add'},
        {id: '#update_emp', contentId: '#manage_employee_update'},
        {id: '#view_emp', contentId: '#manage_employee_view'},
        {id: '#archive_emp', contentId: '#manage_employee_archive'}
    ];
    
    buttons.forEach(button => {
        $(button.id).on('click', function() {
            buttons.forEach(otherButton => {
                if (button === otherButton) {
                    $(otherButton.contentId).css({ display: 'flex', flex: '3' });

                    // Check if the clicked button is #update_emp and toggle #hide_employee_id_input display
                    if (button.id === '#update_emp') {
                        $('#hide_employee_id_input').css('display', 'block');
                    } else {
                        $('#hide_employee_id_input').css('display', 'none');
                    }

                } else {
                    $(otherButton.contentId).css({ display: 'none', flex: '' });
                }
            });
        });
    });
    // function to change container background of view to white on click
     $('#view_emp').click(function(){
        $('#container').addClass('view_emp_section')
    })
    // to compare, go to line 16 of the css, remove the 2 in .vew_emp_section2 and comment the background color in line 165
    // Which of the view is more appealing to you?
    const all_buttons = ['#add_new_emp', '#update_emp', '#archive_emp']
    for (const button of all_buttons){
        $(button).click( () => {
            if ($('#container').hasClass('view_emp_section'))
              $('#container').removeClass('view_emp_section')
        })
    }
   
});