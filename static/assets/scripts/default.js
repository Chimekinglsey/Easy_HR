document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        const notification = document.querySelector('.red_background');
        if (notification) {
            notification.classList.add('fade-out');
        }
        notification.addEventListener.style.display = 'none';
    }, 3000)
    ;
})