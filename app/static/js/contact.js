document.addEventListener("DOMContentLoaded", function () {
    let contactForm = document.getElementById("contactForm");
    if (!contactForm) {
        console.error("❌ contactForm not found!");
        return; // Stop script execution
    }

    contactForm.addEventListener("submit", async function (event) {
        event.preventDefault(); // Stop refresh
        console.log("Form submission started");

        let formData = new FormData(this);
        let responseMessage = document.getElementById("formMessage");
        let submitButton = this.querySelector('button[type="submit"]');
        
        // Get CSRF token from the form
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
        // Show loading state
        submitButton.textContent = "Sending...";
        submitButton.disabled = true;
        responseMessage.innerHTML = `<div class="loading-message">📤 Sending your message...</div>`;

        try {
            let response = await fetch("/", {
                method: "POST",
                body: formData,
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": csrfToken
                }
            });

            let result = await response.json();
            console.log("Response received:", result);

            if (result.success) {
                responseMessage.innerHTML = `<div class="success-message">✅ ${result.message || 'Message sent successfully!'}</div>`;
                responseMessage.style.color = "green";
                this.reset();
                
                // Auto-hide success message after 5 seconds
                setTimeout(() => {
                    responseMessage.innerHTML = "";
                }, 5000);
            } else {
                responseMessage.innerHTML = `<div class="error-message">❌ ${result.error || 'Failed to send message.'}</div>`;
                responseMessage.style.color = "red";
                console.error("Error:", result.error);
            }
        } catch (error) {
            console.error("Fetch error:", error);
            responseMessage.innerHTML = `<div class="error-message">❌ Network error. Please check your connection and try again.</div>`;
            responseMessage.style.color = "red";
        } finally {
            // Reset button state
            submitButton.textContent = "Send Message";
            submitButton.disabled = false;
        }
    });
});
