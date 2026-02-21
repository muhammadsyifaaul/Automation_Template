document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');
    const loginMessage = document.getElementById('loginMessage');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Reset errors
        usernameError.textContent = '';
        passwordError.textContent = '';
        loginMessage.className = 'message hidden';
        loginMessage.textContent = '';
        loginMessage.removeAttribute('data-testid'); // remove old test id

        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();
        let isValid = true;

        if (!username) {
            usernameError.textContent = 'Username is required';
            isValid = false;
        }

        if (!password) {
            passwordError.textContent = 'Password is required';
            isValid = false;
        }

        if (isValid) {
            // Simulated login
            if (username === 'admin' && password === 'password123') {
                loginMessage.textContent = 'Login successful!';
                loginMessage.className = 'message success';
                loginMessage.setAttribute('data-testid', 'successMessage');
            } else {
                loginMessage.textContent = 'Invalid username or password';
                loginMessage.className = 'message error';
                loginMessage.setAttribute('data-testid', 'errorMessage');
            }
        }
    });

    // Clear errors on input
    usernameInput.addEventListener('input', () => {
        usernameError.textContent = '';
    });
    
    passwordInput.addEventListener('input', () => {
        passwordError.textContent = '';
    });
});
