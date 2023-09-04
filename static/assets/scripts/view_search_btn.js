// const employeeSearchForm = document.getElementById('employeeSearchForm');
//     const searchInput = document.getElementById('search_id');
//     const viewEmployeesDiv = document.getElementById('view_employees');

//     // Add a submit event listener to the form
//     employeeSearchForm.addEventListener('submit', function (event) {
//         event.preventDefault(); // Prevent the default form submission

//         // Get the value entered in the input field
//         const searchValue = searchInput.value;

//         // Construct the URL based on the entered value
//         const searchURL = `/view_employee/${searchValue}`;

//         // Fetch data from the server using AJAX
//         fetch(searchURL)
//             .then(response => response.text())
//             .then(data => {
//                 // Update the view_employees div with the response
//                 viewEmployeesDiv.innerHTML = data;
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//             });
//     });

// Get references to the form and input field
addEventListener('DOMContentLoaded', function(){
    const employeeSearchForm = document.getElementById('employeeSearchForm');
    const searchInput = document.getElementById('search_id');

    employeeSearchForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
    let searchValue = searchInput.value;
    alert('read the page at least')
    //    const searchValue = searchInput.value; // Trim to remove leading/trailing spaces
    // let employeeID = $("input[name='employeeID']").val()
    if (searchValue) {
            alert(searchValue);
            const searchURL = `/view_employee/${searchValue}`;
            window.location.href = searchURL;
    }
    else {
        alert('Please enter an employee ID');
    }
    });
})

