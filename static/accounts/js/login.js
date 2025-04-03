document.querySelector("form").addEventListener("submit", function (event) {
    event.preventDefault(); 

    let email = document.querySelector('[name=email]').value;
    let password = document.querySelector('[name=password]').value;

    fetch("api/login/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({email: email, password: password})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Login Successful!");
            window.location.href = "/home";  // Redirect to home page after login
        } else {
            alert("Error: " + data.message);
        }
    })
    .catch(error => console.error("Error:", error));
});
function togglePassword(fieldId) {
    const passwordField = document.getElementById(fieldId);
    const icon = passwordField.nextElementSibling;
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        icon.classList.replace('fa-eye', 'fa-eye-slash');
    } else {
        passwordField.type = 'password';
        icon.classList.replace('fa-eye-slash', 'fa-eye');
    }
}