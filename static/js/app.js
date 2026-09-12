/* =========================================================
   INSTANT MEETING SUMMARISER
   Global JavaScript
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    /* =====================================================
       MOBILE NAVIGATION
       ===================================================== */

    const menuButton = document.querySelector(".mobile-menu-btn");
    const navLinks = document.querySelector(".nav-links");

    if (menuButton && navLinks) {
        menuButton.addEventListener("click", () => {
            navLinks.classList.toggle("open");

            const isOpen = navLinks.classList.contains("open");

            menuButton.setAttribute(
                "aria-expanded",
                isOpen.toString()
            );
        });

        document.addEventListener("click", (event) => {

            if (
                !navLinks.contains(event.target) &&
                !menuButton.contains(event.target)
            ) {
                navLinks.classList.remove("open");

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );
            }

        });
    }


    /* =====================================================
       SCROLL REVEAL
       ===================================================== */

    const revealElements =
        document.querySelectorAll(".reveal");

    if ("IntersectionObserver" in window) {

        const observer = new IntersectionObserver(
            (entries) => {

                entries.forEach((entry) => {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("visible");

                        observer.unobserve(entry.target);
                    }

                });

            },
            {
                threshold: 0.12
            }
        );

        revealElements.forEach((element) => {
            observer.observe(element);
        });

    } else {

        revealElements.forEach((element) => {
            element.classList.add("visible");
        });

    }


    /* =====================================================
       BUTTON LOADING STATE
       ===================================================== */

    const loadingForms =
        document.querySelectorAll(
            "form[data-loading]"
        );

    loadingForms.forEach((form) => {

        form.addEventListener("submit", () => {

            const button =
                form.querySelector(
                    "button[type='submit']"
                );

            if (!button) return;

            button.classList.add("loading");
            button.disabled = true;

        });

    });


    /* =====================================================
       AUTO DISMISS ALERTS
       ===================================================== */

    const alerts =
        document.querySelectorAll(
            ".alert[data-auto-dismiss]"
        );

    alerts.forEach((alert) => {

        setTimeout(() => {

            alert.style.opacity = "0";
            alert.style.transform = "translateY(-10px)";

            setTimeout(() => {
                alert.remove();
            }, 300);

        }, 4000);

    });


    /* =====================================================
       COPY TO CLIPBOARD
       ===================================================== */

    document.querySelectorAll(
        "[data-copy]"
    ).forEach((button) => {

        button.addEventListener("click", async () => {

            const selector =
                button.getAttribute("data-copy");

            const element =
                document.querySelector(selector);

            if (!element) return;

            try {

                await navigator.clipboard.writeText(
                    element.innerText
                );

                const originalText =
                    button.innerText;

                button.innerText = "Copied ✓";

                setTimeout(() => {
                    button.innerText =
                        originalText;
                }, 1800);

            } catch (error) {

                console.error(
                    "Copy failed:",
                    error
                );

            }

        });

    });


    /* =====================================================
       SMOOTH ANCHOR SCROLL
       ===================================================== */

    document.querySelectorAll(
        'a[href^="#"]'
    ).forEach((link) => {

        link.addEventListener("click", (event) => {

            const targetId =
                link.getAttribute("href");

            if (
                !targetId ||
                targetId === "#"
            ) {
                return;
            }

            const target =
                document.querySelector(targetId);

            if (!target) return;

            event.preventDefault();

            target.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        });

    });


    /* =====================================================
       PASSWORD VISIBILITY
       ===================================================== */

    document.querySelectorAll(
        "[data-password-toggle]"
    ).forEach((button) => {

        button.addEventListener("click", () => {

            const inputId =
                button.getAttribute(
                    "data-password-toggle"
                );

            const input =
                document.getElementById(inputId);

            if (!input) return;

            if (input.type === "password") {

                input.type = "text";
                button.innerText = "Hide";

            } else {

                input.type = "password";
                button.innerText = "Show";

            }

        });

    });


    /* =====================================================
       CONFIRM ACTIONS
       ===================================================== */

    document.querySelectorAll(
        "[data-confirm]"
    ).forEach((element) => {

        element.addEventListener("click", (event) => {

            const message =
                element.getAttribute(
                    "data-confirm"
                );

            if (
                message &&
                !window.confirm(message)
            ) {
                event.preventDefault();
            }

        });

    });

});