function validateForm(){
    var errMessage="";
    var flag=0;
    var age = document.getElementById('ageIn').value;
    var height = document.getElementById('heightIn').value;
    var weight = document.getElementById('weightIn').value;

    var gender="";
    if (document.getElementById('male').checked)
        gender +='male';
    if (document.getElementById('female').checked)
        gender +='female';

    var goal="";
    if (document.getElementById('fatloss').checked)
        goal += 'fatloss';
    if (document.getElementById('maintenance').checked)
        goal += 'maintenance';
    if (document.getElementById('muscleGain').checked)
        goal += 'muscleGain';

    var activity="";
    if (document.getElementById('light').checked)
        activity += 'light';
    if (document.getElementById('moderate').checked)
        activity += 'moderate';
    if (document.getElementById('high').checked)
        activity += 'high';
    
    if (age == "")
    {
        errMessage +="Enter Age\n";
        document.getElementById('age').style.color="red";
        flag++;
    }
    else if (isNaN(age))
    {
        errMessage += "Age should be a numerical value\n";
        document.getElementById('age').style.color="red";
        flag++;
    }
    if (height == "")
    {
        errMessage +="Enter Height\n";
        document.getElementById('height').style.color="red";
        flag++;
    }
    else if (isNaN(height))
    {
        errMessage += "Height should be a numerical value\n";
        document.getElementById('height').style.color="red";
        flag++;
    }
    if (weight == "")
    {
        errMessage +="Enter Weight\n";
        document.getElementById('weight').style.color="red";
        flag++;
    }
    else if (isNaN(weight))
    {
        errMessage += "Weight should be a numerical value\n";
        document.getElementById('weight').style.color="red";
        flag++;
    }
    if (gender == "")
    {
        errMessage += "Please select your gender";
        document.getElementById('gender').style.color="red";
        flag++;
    }
    if (goal == "")
    {
        errMessage += "Please select your goal";
        document.getElementById('goal').style.color="red";
        flag++;
    }
    if (activity == "")
    {
        errMessage +="Please select your activity level";
        document.getElementById('activity').style.color="red";
        flag++;
    }
    if (flag==0)
        return true;
    else    
        return false;
}
document.getElementById('ageIn').addEventListener("click", function(){
    document.getElementById('age').style.color="white";
});
document.getElementById('female').addEventListener("click", function(){
    document.getElementById('gender').style.color="white";
});
document.getElementById('male').addEventListener("click", function(){
    document.getElementById('gender').style.color="white";
});
document.getElementById('heightIn').addEventListener("click", function(){
    document.getElementById('height').style.color="white";
});
document.getElementById('weightIn').addEventListener("click", function(){
    document.getElementById('weight').style.color="white";
});
document.getElementById('fatloss').addEventListener("click", function(){
    document.getElementById('goal').style.color="white";
});
document.getElementById('maintenance').addEventListener("click", function(){
    document.getElementById('goal').style.color="white";
});
document.getElementById('muscleGain').addEventListener("click", function(){
    document.getElementById('goal').style.color="white";
});
document.getElementById('light').addEventListener("click", function(){
    document.getElementById('activity').style.color="white";
});
document.getElementById('moderate').addEventListener("click", function(){
    document.getElementById('activity').style.color="white";
});
document.getElementById('high').addEventListener("click", function(){
    document.getElementById('activity').style.color="white";
});