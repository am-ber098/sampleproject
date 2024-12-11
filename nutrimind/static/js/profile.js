const saveButton = document.getElementById('saveProfileButton');
if (saveButton) {
    saveButton.addEventListener('click', async function() {
        
        const profileData = {
            name: "{{ user_profile.name }}",  // Get user name
            age: "{{ user_profile.age }}",    // Get user age
            weight: "{{ user_profile.weight }}", // Get user weight
            psychological_condition: document.querySelector('select[name="psychological_condition"]').value  //dropdown value
        };

        try {
            // it will send the collected data to the server
            const response = await fetch("{% url 'save_profile' %}", {
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(profileData)
            });

            // Handle response from  server
            if (response.ok) {
                // Redirect to saveprofile.html page on successful save
                window.location.href = "{% url 'save_profile' %}";
            } else {
                alert('Error saving the profile');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An unexpected error occurred.');
        }
    });
}
