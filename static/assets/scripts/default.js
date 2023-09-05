document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        const notification = document.querySelector('.flash_messages');
        if (notification) {
            notification.classList.add('fade-out');
        }
    }, 4000);
})