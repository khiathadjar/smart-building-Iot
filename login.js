document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    // On récupère les valeurs (vérifie bien que les IDs existent dans le HTML)
    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    try {
        const res = await fetch("http://localhost:8000/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await res.json();

        if (res.ok) {
            alert("Connexion réussie !");
            // ✅ C'EST CETTE LIGNE QUI MANQUAIT :
            window.location.href = "index.html"; 
        } else {
            alert("Erreur : " + (data.detail || "Identifiants invalides"));
        }
    } catch (error) {
        console.error("Erreur réseau :", error);
        alert("Impossible de contacter le serveur.");
    }
});