// Generate a random captcha code (simple text-based)
function generateCaptchaCode() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let captchaCode = '';
    
    for (let i = 0; i < 6; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        captchaCode += characters.charAt(randomIndex);
    }
    
    return captchaCode;
}

// Update the captcha text and display it
function refreshCaptcha() {
    const captchaCode = generateCaptchaCode();
    const captchaImage = document.getElementById('captchaImage');
    
    // Display the captcha text instead of an image
    captchaImage.innerText = captchaCode;

    return captchaCode;
}

// Attach event listeners when the document is loaded
document.addEventListener('DOMContentLoaded', function () {
    const refreshCaptchaButton = document.getElementById('refreshCaptcha');
    const captchaInput = document.getElementById('captchaInput');

    // Refresh the captcha when the page loads
    const captchaCode = refreshCaptcha();

    // Attach click event listener to the refresh button
    refreshCaptchaButton.addEventListener('click', function () {
        captchaInput.value = ''; // Clear previous input
        refreshCaptcha(); // Refresh the captcha
    });

    // Attach input event listener to the captcha input for validation (you can customize this logic)
    captchaInput.addEventListener('input', function () {
        const enteredCode = captchaInput.value;
        if (enteredCode.toLowerCase() === captchaCode.toLowerCase()) {
            // Captcha code is correct
            // You can add additional validation logic here
        }
    });
});
