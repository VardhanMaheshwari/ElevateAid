document.addEventListener("DOMContentLoaded", function () {
    fetch("/api/home/", {
        method: "GET",
        credentials: "include" 
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Unauthorized Access");
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("welcomeMessage").innerText = "Welcome, " + data.user;

        // Redirect to respective homepage based on user type
        if (data.user_type === "donor") {
            window.location.href = "/donor_home/";
        } else if (data.user_type === "receiver") {
            window.location.href = "/receiver_home/";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Session expired. Please log in again.");
        window.location.href = "{% url 'login_view' %}";
    });
});

function logout() {
    fetch("/api/logout/", {
        method: "POST",
        credentials: "include"
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        window.location.href = "{% url 'login_view' %}";
    })
    .catch(error => console.error("Error:", error));
}
