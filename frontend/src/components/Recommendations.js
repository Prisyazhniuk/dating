import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Recommendations() {
    const [recommendations, setRecommendations] = useState([]);

    useEffect(() => {
        const fetchRecommendations = async () => {
            try {
                const userId = 1; // Replace with actual user ID
                const response = await axios.get(`/api/recommendations/${userId}/`);
                setRecommendations(response.data);
            } catch (error) {
                console.error(error);
            }
        };

        fetchRecommendations();
    }, []);

    return (
        <div>
            <h1>Recommendations</h1>
            <ul>
                {recommendations.map(user => (
                    <li key={user.id}>{user.username}</li>
                ))}
            </ul>
        </div>
    );
}

export default Recommendations;
