function validateCitizenStep()
{
	var account_type = document.getElementById('account_type').value;

	var Error='Please attend to the following! \n';
	var Errorcount = 0;

	if(account_type === '')
	{
		Error +='--Select the type of account! \n';
		Errorcount +=1;
	}

	if(Errorcount === 0)
	{
		return true;

	}
	else
	{
		alert(Error);
		return false;
	}
}

function validateCitizenStep1()
{
	var id_number = document.getElementById('id_number').value;

	var first_name = document.getElementById('first_name').value;
		//alert ("step1");
	//alert (first_name);
	var surname = document.getElementById('surname').value;
	var last_name = document.getElementById('last_name').value;
	var gender = document.getElementById('gender').value;
	var countryId = document.getElementById('countryId').value;
	var account_type = document.getElementById('account_type').value;

	var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;//regex for testing valid emails
	var int= /[0-9]/;
	var char=/^.*[A-Za-z’`{|}~]+.*$/;
	//phonenum=/^[\+]?[(]?[0-9]{3}[)]?[-\s\.*]?[0-9]{3}[-\s\.*]?[0-9]{4,9}$/;
	var phonenum=/^.*[\+]?[(]?[0-9]{1,3}[)]?[-\s\.*]?[0-9]{1,3}[-\s\.*]?[0-9]{4,9}$/;
	vardateregex=/^(0?[1-9]|[12][0-9]|3[01])[- /.*](0[1-9]|1[012])[- /.*](19|20)\d\d$/;
	var spechar = /^\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\+|\=|\[|\{|\]|\}|\||\\|\'|\<|\,|\.|\>|\?|\/|\""|\;|\:|\$/;

	var Error='Please attend to the following! \n';
	var Errorcount = 0;

	if( (account_type=='citizen') && (id_number === '' || !int.test(id_number) || spechar.test(id_number)))
	{
		Error +='--Enter ID Number as Intergers only ! \n';
		Errorcount +=1;
	}
	if( (account_type=='foreigner') && (id_number === '' || !int.test(id_number) || spechar.test(id_number)))
	{
		Error +='--Enter Alien Card Number as Intergers only ! \n';
		Errorcount +=1;
	}
	if( (account_type=='other') && (id_number === '' || spechar.test(id_number)))
	{
		Error +='--Enter Passport Number ! \n';
		Errorcount +=1;
	}
	if(first_name === '' ||!char.test(first_name))
	{
		Error +='--Enter first name as Characters only please! \n';
		Errorcount +=1;
	}
	if(last_name === '' ||!char.test(last_name))
	{
		Error +='--Enter last name as Characters only please! \n';
		Errorcount +=1;
	}
	if(gender === '' )
	{
		Error +='--Select the gender! \n';
		Errorcount +=1;
	}
	if(countryId === '' )
	{
		Error +='--Select country! \n';
		Errorcount +=1;
	}

	if(Errorcount === 0)
	{
		return true;

	}
	else
	{
		alert(Error);
		return false;
	}
}

function validateCitizenStep2()
{
	var id_number = document.getElementById('id_number').value;
	var phone_no = document.getElementById('phone_no').value;
	var email_address = document.getElementById('email_address').value;
	var confirm_email_address = document.getElementById('confirm_email_address').value;
	var password = document.getElementById('password').value;
	var confirm_password = document.getElementById('confirm_password').value;

	var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;//regex for testing valid emails
	var int= /[0-9]/;
	var char=/^.*[A-Za-z’`{|}~]+.*$/;
	//phonenum=/^[\+]?[(]?[0-9]{3}[)]?[-\s\.*]?[0-9]{3}[-\s\.*]?[0-9]{4,9}$/;
	var phonenum=/^.*[\+]?[(]?[0-9]{1,3}[)]?[-\s\.*]?[0-9]{1,3}[-\s\.*]?[0-9]{4,9}$/;
	var lower = /[a-z]/;
	var upper = /[A-Z]/;

	var Error='Please attend to the following! \n';
	var Errorcount = 0;

	var uploadImg = document.getElementById('profilePhotoUploadFile');
	/*
	if(uploadImg.files.length<1)
	{
		Error +='--Select a profile photo! \n';
		Errorcount +=1;
	}
	*/
	for (var i = 0; i < uploadImg.files.length; i++) {
       var f = uploadImg.files[i];
       if (endsWith(f.name, 'jpg') || endsWith(f.name, 'png') || endsWith(f.name, 'jpeg') || endsWith(f.name, 'JPEG') || endsWith(f.name, 'JPG') || endsWith(f.name, 'PNG') || endsWith(f.name, 'gif') || endsWith(f.name, 'GIF') ) {

       }else
	   {
		   Error +='--'+f.name+' has a wrong file format! only jpg,png,jpeg,gif are allowed \n';
		   Errorcount +=1;
	   }
    }

	for (var i = 0; i < uploadImg.files.length; i++) {
       var f = uploadImg.files[i];
       if (f.size>2097152) {
           Error +='--'+f.name+' file is too large! Max size is 2MB \n';
		   Errorcount +=1;
       }
    }

	/*if(id_number === '' ||!int.test(id_number))
	{
		Error +='--Enter ID Number as numeric only please! \n';
		Errorcount +=1;
	}
	*/
	if(phone_no === '' ||!phonenum.test(phone_no))
	{
		Error +='--Enter a valid phone number! \n';
		Errorcount +=1;
	}
	if(email_address === '' ||!filter.test(email_address))
	{
		Error +='--Enter a valid email address! \n';
		Errorcount +=1;
	}
	if(email_address !== confirm_email_address )
	{
		Error +='--Email address do not match ! \n';
		Errorcount +=1;
	}
	if(password === '' )
	{
		Error +='--Enter password! \n';
		Errorcount +=1;
	}
	if(password.length<6 )
	{
		Error +='--Password should be atleast 6 characters long! \n';
		Errorcount +=1;
	}
	if(!lower.test(password))
	{
		Error +='--Error: password must contain at least one lowercase letter (a-z)! \n';
		Errorcount +=1;
	}
	if(!upper.test(password))
	{
		Error +='--Error: password must contain at least one uppercase letter (A-Z)! \n';
		Errorcount +=1;
	}
	if(confirm_password === '' )
	{
		Error +='--Enter password confirmation! \n';
		Errorcount +=1;
	}
	if(password !== confirm_password )
	{
		Error +='--Passwords do not match ! \n';
		Errorcount +=1;
	}


	if(Errorcount === 0)
	{
		return true;

	}
	else
	{
		alert(Error);
		return false;
	}
}

function readURLPhoto(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#profilePhoto')
                        .attr('src', e.target.result)
                        .width(100)
                        .height(100);
                };

                reader.readAsDataURL(input.files[0]);
            }
        }

function endsWith(str, suffix) {
   return str.indexOf(suffix, str.length - suffix.length) !== -1;
}

function validateChangePassword()
{
	var token = document.getElementById('token').value;
	var password = document.getElementById('password').value;
	var confirm_password = document.getElementById('confirm_password').value;

	var lower = /[a-z]/;
	var upper = /[A-Z]/;

	var Error='Please attend to the following! \n';
	var Errorcount = 0;

	if(token === '' )
	{
		Error +='--Error getting password change token! \n';
		Errorcount +=1;
	}
	if(password === '' )
	{
		Error +='--Enter password! \n';
		Errorcount +=1;
	}
	if(password.length<6 )
	{
		Error +='--Password should be atleast 6 characters long! \n';
		Errorcount +=1;
	}
	if(!lower.test(password))
	{
		Error +='--Error: password must contain at least one lowercase letter (a-z)! \n';
		Errorcount +=1;
	}
	if(!upper.test(password))
	{
		Error +='--Error: password must contain at least one uppercase letter (A-Z)! \n';
		Errorcount +=1;
	}
	if(confirm_password === '' )
	{
		Error +='--Enter password confirmation! \n';
		Errorcount +=1;
	}
	if(password !== confirm_password )
	{
		Error +='--Passwords do not match ! \n';
		Errorcount +=1;
	}


	if(Errorcount === 0)
	{
		return true;

	}
	else
	{
		alert(Error);
		return false;
	}
}