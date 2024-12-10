// script.js
document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('clickButton');
    const message = document.getElementById('message');

    button.addEventListener('click', () => {
        message.innerText = 'You clicked the button! Hello, World!';
    });
});
