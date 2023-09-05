// document.addEventListener('DOMContentLoaded', function() {
//     setTimeout(function() {
//         const notification = document.querySelector('.red_background');
//         if (notification) {
//             notification.classList.add('fade-out');
//             notification.addEventListener.style.display = 'none';

//         }
//     }, 3000);
// })
document.addEventListener('DOMContentLoaded', function() {
    const notification = document.querySelector('.red_background');

    if (notification) {
        setTimeout(function() {
            notification.classList.add('fade-out');

            // Listen for the transition end event to remove the element
            notification.addEventListener('transitionend', function() {
                notification.style.display = 'none';
            });
        }, 3000);
    }
});