// =====================
// REGISTER USER
// =====================
async function registerUser() {

    const name =
        document.getElementById("name").value;

    const email =
        document.getElementById(
            "registerEmail"
        ).value;

    const password =
        document.getElementById(
            "registerPassword"
        ).value;

    const userData = {
        name: name,
        email: email,
        password: password
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/register",
            {
                method: "POST",
                headers: {
                    "Content-Type":
                        "application/json"
                },
                body: JSON.stringify(userData)
            }
        );

        const data =
            await response.json();

        alert(data.message);

        window.location.href =
            "login.html";

    } catch (error) {

        console.log(error);

        alert(
            "Registration Failed"
        );
    }
}


// =====================
// LOGIN USER
// =====================
async function loginUser() {

    const email =
        document.getElementById(
            "email"
        ).value;

    const password =
        document.getElementById(
            "password"
        ).value;

    const loginData = {
        name: "",
        email: email,
        password: password
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/login",
            {
                method: "POST",

                credentials: "include",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify(
                    loginData
                )
            }
        );

        const data =
            await response.json();

        if (response.ok) {

            alert(
                data.message
            );

            window.location.href =
                "dashboard.html";

        } else {

            alert(
                data.detail
            );
        }

    } catch (error) {

        console.log(error);

        alert(
            "Login Failed"
        );
    }
}


// =====================
// CHECK PROFILE
// =====================
async function checkProfile() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/profile",
            {
                credentials:
                    "include"
            }
        );

        const data =
            await response.json();

        if (response.ok) {

            document.getElementById(
                "welcome"
            ).innerHTML =
                data.message;

        } else {

            window.location.href =
                "login.html";
        }

    } catch (error) {

        console.log(error);
    }
}


// =====================
// LOGOUT
// =====================
async function logout() {

    await fetch(
        "http://127.0.0.1:8000/logout",
        {
            method: "POST",
            credentials:
                "include"
        }
    );

    window.location.href =
        "login.html";
}