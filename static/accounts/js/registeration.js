document.querySelector("form").addEventListener("submit", function (event) {
    event.preventDefault();  // Prevent default form submission

    let formData = new FormData(this);
    let jsonData = {}; 
    console.log(formData)
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    console.log("Collected JSON Data:", JSON.stringify(jsonData))

    fetch("/api/register/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json" // JSON request format
        },
        body: JSON.stringify(jsonData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Registration Successful!");
            window.location.href = "";  // Redirect to login page
        } else {
            alert("Error: " + data.message);
        }
    })
    .catch(error => console.error("Error:", error));
});

const userTypeSelect = document.getElementById("user_type");
const subTypeSelect = document.getElementById("sub_type");
const companyFields = document.getElementById("company_fields");
const companyLogo = document.getElementById("company_logo");
const personalFields = document.getElementById("personal_fields");

// Mapping user type to sub-type options
const subTypeOptions = {
    beneficiary: ["NGO", "College"],
    donor: ["Company", "Personal"]
};

userTypeSelect.addEventListener("change", function () {
    const userType = this.value;
    subTypeSelect.innerHTML = '<option value="" selected disabled>Select Sub-Type</option>';
    console.log(subTypeOptions[userType]);
    if (subTypeOptions[userType]) {
        subTypeOptions[userType].forEach(option => {
            const newOption = document.createElement("option");
            newOption.value = option.toLowerCase();
            newOption.textContent = option;
            subTypeSelect.appendChild(newOption);
        });
    }

    // Hide all conditional fields initially
    console.log(companyFields.classList);
    companyFields.classList.add("hidden");
    companyLogo.classList.add("hidden");
    personalFields.classList.add("hidden");
});

subTypeSelect.addEventListener("change", function () {
    const subType = this.value;

    // Hide all optional fields first
    companyFields.classList.add("hidden");
    companyLogo.classList.add("hidden");
    personalFields.classList.add("hidden");
    

    if (["ngo", "college", "company"].includes(subType)) {
        companyFields.classList.remove("hidden");
        companyLogo.classList.remove("hidden");
    } else if (subType === "personal") {
        personalFields.classList.remove("hidden");
    }
});
function togglePassword() {
    const passwordField = document.getElementById('password');
    const icon = document.querySelector('.password-toggle');
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        icon.classList.replace('fa-eye', 'fa-eye-slash');
    } else {
        passwordField.type = 'password';
        icon.classList.replace('fa-eye-slash', 'fa-eye');
    }
}