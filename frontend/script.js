const API = "https://job-tracker-api.onrender.com";

// ✅ Load token from localStorage
let token = localStorage.getItem("token") || "";


// =========================
// REGISTER
// =========================
async function register() {
    const email = document.getElementById("regEmail").value;
    const password = document.getElementById("regPassword").value;

    const res = await fetch(`${API}/register`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({email, password})
    });

    if (res.ok) {
        alert("Registered successfully!");
    } else {
        alert("Registration failed");
    }
}


// =========================
// LOGIN
// =========================
async function login() {
    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    const res = await fetch(`${API}/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({email, password})
    });

    const data = await res.json();

    if (data.access_token) {
        token = data.access_token;

        // ✅ Save token
        localStorage.setItem("token", token);

        alert("Login successful!");
    } else {
        alert("Login failed");
    }
}


// =========================
// LOGOUT
// =========================
function logout() {
    localStorage.removeItem("token");
    token = "";
    alert("Logged out");
}


// =========================
// ADD JOB
// =========================
async function addJob() {
    if (!token) {
        alert("Please login first!");
        return;
    }

    const company = document.getElementById("company").value;
    const role = document.getElementById("role").value;
    const status = document.getElementById("status").value;

    await fetch(`${API}/jobs`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({company, role, status})
    });

    alert("Job added!");
    getJobs();
}


// =========================
// GET JOBS
// =========================
async function getJobs() {
    if (!token) {
        alert("Please login first!");
        return;
    }

    const res = await fetch(`${API}/jobs`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const jobs = await res.json();

    const list = document.getElementById("jobList");
    list.innerHTML = "";

    jobs.forEach(job => {
        const li = document.createElement("li");
        li.innerHTML = `
            <b>${job.company}</b> - ${job.role} 
            <br>Status: ${job.status}
        `;
        list.appendChild(li);
    });
}