const input_username = document.querySelector('#exampleInputUsername1');
const input_email = document.querySelector('#exampleInputEmail1');
const username_invalid = document.querySelector('.username-invalid-feedback')
const email_invalid = document.querySelector('.email-invalid-feedback')
const username_valid = document.querySelector('.valid-username')
const email_valid = document.querySelector('.valid-email')
const register_btn = document.querySelector('.register-btn')

input_username.addEventListener("keyup", (e) => {
    const username_value = e.target.value;

    username_valid.style.display = 'block';
    username_valid.textContent = `Checking...`;

    input_username.classList.remove('is-invalid');
    username_invalid.style.display = 'none';

    if (username_value.length > 0) {
        fetch('/validate-username/', {
            body: JSON.stringify({username: username_value}),
            method: 'POST',
        }).then(res => res.json()).then(data => {
            console.log('data:', data);
            username_valid.style.display = 'none';
            if (data.username_error) {
                input_username.classList.add('is-invalid');
                username_invalid.style.display = 'block';
                username_invalid.innerHTML = `<p>${data.username_error}</p>`;
                register_btn.disabled = true;
            }
            else{
                register_btn.removeAttribute('disabled');
            }
        });
    }
});

input_email.addEventListener("keyup", (e) => {
    const email_value = e.target.value;

    input_email.classList.remove('is-invalid');
    email_invalid.style.display = 'none';

    if (email_value.length > 0) {
        fetch('/validate-email/', {
            body: JSON.stringify({email: email_value}),
            method: 'POST',
        }).then(res => res.json()).then(data => {
            console.log('data:', data);
            if (data.email_error) {
                register_btn.disabled = true;
                input_username.classList.add('is-invalid');
                email_invalid.style.display = 'block';
                email_invalid.innerHTML = `<p>${data.email_error}</p>`
            } else {
                register_btn.removeAttribute('disabled');
            }
        });
    }
});


