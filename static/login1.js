function validateform() {
    var name = document.myform.name.value;
    var dept = document.myform.dept.value
    var phno = document.myform.phno.value;

    var club = document.myform.club.value;
    
    if (dept == null || dept == "") {
        alert("Dept Name can't be blank");
        return false;
    }

    if (name == null || name == "") {
        alert("Event Name can't be blank");
        return false;
    }

    if (club == null || club == "") {
        alert("Event Name can't be blank");
        return false;
    }


    if (phno.length != 10) {
        alert("Please enter a valid phone number");
        return false;
    }

    

}



   