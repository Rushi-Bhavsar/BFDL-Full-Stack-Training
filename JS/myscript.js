var fname = prompt("Enter First name: ")
var lname = prompt("Enter Last name: ")
var age = prompt("Enter age: ")
var height = prompt("Enter height in cm: ")
var pet_name = prompt("Enter Pet Name: ")
if (fname[0] === lname[0] && 20 <= age <= 30 && height > 170 && pet_name.slice(-1) === "y" )
    console.log("Welcome spy. Your next mission will assigned shortly.")
else
    console.log("Restricted area."+fname[0] , lname[0], age, height, pet_name[-1])


