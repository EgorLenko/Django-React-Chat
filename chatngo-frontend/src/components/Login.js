import React, {useState} from "react";
import {Link} from "react-router-dom";
import PropTypes from "prop-types";
import styles from './style/Login.module.css';

const Login = ({onLogin}) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);

    const handleInputChange = (setter) => (event) => {
        setter(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch("http://localhost:8000/dj-auth/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({username, password}),
            });

            if (!response.ok) {
                throw new Error("Invalid credentials");
            }

            const data = await response.json();
            onLogin(username, data.access);
        } catch (err) {
            setError(err.message);
        }
    };

    return (
        <section>
            <div className={styles.loginBox}>
                <h1>Login</h1>
                {error && <div className={`${styles.alert} ${styles.alertDanger}`}>{error}</div>}
                <form onSubmit={handleSubmit}>
                    <div className={styles.formGroup}>
                        <label htmlFor="username">Username </label>
                        <input
                            type="text"
                            id="username"
                            className={styles.formControl}
                            value={username}
                            onChange={handleInputChange(setUsername)}
                        />
                    </div>
                    <div className={styles.formGroup}>
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            id="password"
                            className={styles.formControl}
                            value={password}
                            onChange={handleInputChange(setPassword)}
                        />
                    </div>
                    <div className="forget">
                        <label htmlFor=""><input type="checkbox"/>Remember me</label>
                        <a href="#">Forget password </a>
                    </div>
                    <button type="submit" className={`${styles.btn} ${styles.btnPrimary}`}>
                        Login
                    </button>
                    <div className="register">
                        <p>
                            Don&apos;t have an account? <Link to="/register">Register</Link>
                        </p>
                    </div>
                </form>
            </div>
        </section>
    );
};

Login.propTypes = {
    onLogin: PropTypes.func.isRequired,
};

export default Login;