import React, { useState } from 'react';
import axios from 'axios';

const Register = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
    });

    const { username, email, password, confirmPassword } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = async e => {
        e.preventDefault();
        if (password !== confirmPassword) {
            alert('Passwords do not match');
        } else {
            const newUser = {
                username,
                email,
                password
            };
            try {
                const config = {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                };
                const body = JSON.stringify(newUser);
                const res = await axios.post('/api/register', body, config);
                console.log(res.data);
            } catch (err) {
                console.error(err.response.data);
            }
        }
    };

    return (
        <form onSubmit={onSubmit}>
            <div>
                <input type="text" placeholder="Username" name="username" value={username} onChange={onChange} required />
            </div>
            <div>
                <input type="email" placeholder="Email" name="email" value={email} onChange={onChange} required />
            </div>
            <div>
                <input type="password" placeholder="Password" name="password" value={password} onChange={onChange} required />
            </div>
            <div>
                <input type="password" placeholder="Confirm Password" name="confirmPassword" value={confirmPassword} onChange={onChange} required />
            </div>
            <button type="submit">Register</button>
        </form>
    );
};

export default Register;
