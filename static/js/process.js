function create_order(){
	error = document.getElementById('error-meso')
	if(document.getElementById('description').value.length >= 50){
		payload = {
			product: document.getElementById('product-name').value,
			pickup: document.getElementById('pickup').value,
			destination: document.getElementById('destination').value,
			description: document.getElementById('description').value,
			weight: parseInt(document.getElementById('product-weight').value)
		}

		fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels", {
	        method: 'POST',
	        headers: {
	            'Content-Type': 'application/json',
	            'Accept': 'application/json',
	            'token': localStorage.getItem('token')
	        },
	        body: JSON.stringify(payload)
	    })
	    .then(res => res.json())
	    .then(function(data){

	        if (data['status'] == 'failure'){
	            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
	            error.style.display = "block";
	        }else{
	            error.innerHTML = "<strong>Info! </strong> parcel delivery order successfully created";
	            error.style.background = "#16a085";
	            error.style.display = "block";
	        }
	        setTimeout(function(){
	            error.style.display = "none";
	        }, 3000)
	    })
	}else{
		error.innerHTML = "<strong>Error! </strong> description should be more than 50 characters.";
	    error.style.display = "block";

	    setTimeout(function(){
            error.style.display = "none";
        }, 3000)
	}
}

if (/user/.test(window.location.href) && /list.html/.test(window.location.href)){
	fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'token': localStorage.getItem('token')
        }
    })
    .then(res => res.json())
    .then(function(data){
        error = document.getElementById('error-meso')

        if (data['status'] == 'failure'){
            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
            error.style.display = "block";
        }else{
            var table = '';
            table += `
            	<table>
	                <thead>
	                    <tr>
	                        <td style="width: 10%;">Image</td>
	                        <td>Product Description</td>
	                        <td class="rgt">Date Created</td>
	                    </tr>
	                </thead>
	                <tbody>
            `

            order = '';
            for (var i = 0; i < (data['data']).length; i ++){
            	order += "<tr><td><img src='../../static/img/parcel.png' /></td>";
            	order += "<td><a href='single.html?order="+data['data'][i]['order_id']+"'>"+ data['data'][i]['description']+"</a></td>";
            	order += "<td class='rgt'><small>"+data['data'][i]['order_date']+"</small></td>"
            }
            order += '';

            table += order
            table += `
            		</tbody>
            	</table>
            `
            document.getElementById('order-list').innerHTML = table
        }
    })
}

if (/user/.test(window.location.href) && /single.html/.test(window.location.href)){

	var uri = window.location.href
	var url = new URL(uri)
	var order_id = url.searchParams.get("order")
	
	fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels/"+order_id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'token': localStorage.getItem('token')
        }
    })
    .then(res => res.json())
    .then(function(data){
        error = document.getElementById('error-meso')
        if (data['status'] == 'failure'){
            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
            error.style.display = "block";
        }else{
        	var single = `
        		<p id="error-meso"></p>
        		<img src="../../static/img/parcel.png" />
	            <div class="abt-cont">
	        `
	        single += "<p><strong>status : </strong> <small id='status'>"+data['data']['order_status']+"</small></p>"
	        single += "<p><strong>Pickup : </strong> <small>"+data['data']['pickup']+"</small></p>"
	        single += "<p><strong>Present : </strong> <small>"+data['data']['present']+"</small></p>"
	        single += "<p><strong>Destination : </strong> <small id='area'>"+data['data']['destination']+"</small></p>"
			single += "<p>"+data['data']['description']+"</p>"
	        single += `
	                <p class="text">
	                    <button onclick="changedesination()" class="success">Change Destination</button>
	                    <button onclick="cancelorder()" class="danger">Cancel Delivery</button>
	                </p>
	            </div>
        	`
        	document.getElementById('single-order').innerHTML = single
        	setTimeout(function(){
	            error.style.display = "none";
	        }, 3000)
        }
    })
}

function change_destination(){
	error = document.getElementById('error-meso')
	if (document.getElementById("destination").value != ''){
		var uri = window.location.href
		var url = new URL(uri)
		var order_id = url.searchParams.get("order")

		payload = {
			data: document.getElementById("destination").value
		}
		
		fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels/"+order_id+"/destination", {
	        method: 'PUT',
	        headers: {
	            'Content-Type': 'application/json',
	            'Accept': 'application/json',
	            'token': localStorage.getItem('token')
	        },
	        body: JSON.stringify(payload)
	    })
	    .then(res => res.json())
	    .then(function(data){
	        if (data['status'] == 'failure'){
	            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
	            error.style.display = "block";
	            setTimeout(function(){
		            error.style.display = "none";
		        }, 3000)
	        }else{
	        	document.getElementById('area').innerHTML = document.getElementById("destination").value
	        }
	    })
	    lgn.style.display = "none";
	}else{
		error.innerHTML = "<strong>Error! </strong> destination cannot be empty.";
	    error.style.display = "block";
	    lgn.style.display = "none";
	    setTimeout(function(){
            error.style.display = "none";
        }, 3000)
	}
}


function cancelorder(){
	var uri = window.location.href
	var url = new URL(uri)
	var order_id = url.searchParams.get("order")
	
	fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels/"+order_id+"/cancel", {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'token': localStorage.getItem('token')
        }
    })
    .then(res => res.json())
    .then(function(data){
        error = document.getElementById('error-meso')
        if (data['status'] == 'failure'){
            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
            error.style.display = "block";
	            error.style.display = "none";
            setTimeout(function(){
	        }, 3000)
        }else{
        	document.getElementById('status').innerHTML = 'cancelled'
        }
    })
    lgn.style.display = "none";	
}


if (/admin/.test(window.location.href) && /list.html/.test(window.location.href)){
	fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'token': localStorage.getItem('token')
        }
    })
    .then(res => res.json())
    .then(function(data){
        error = document.getElementById('error-meso')

        if (data['status'] == 'failure'){
            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
            error.style.display = "block";
        }else{
            var table = '';
            table += `
            	<table>
	                <thead>
	                    <tr>
	                        <td style="width: 10%;">Image</td>
	                        <td>Username</td>
	                        <td>Product Description</td>
	                        <td class="rgt">Date Created</td>
	                    </tr>
	                </thead>
	                <tbody>
            `

            order = '';
            for (var i = 0; i < (data['data']).length; i ++){
            	order += "<tr><td><img src='../../static/img/parcel.png' /></td>";
            	order += "<td>"+data['data'][i]['username']+"</td>";
            	order += "<td><a href='single.html?order="+data['data'][i]['order_id']+"'>"+ data['data'][i]['description']+"</a></td>";
            	order += "<td class='rgt'><small>"+data['data'][i]['order_date']+"</small></td>"
            }
            order += '';

            table += order
            table += `
            		</tbody>
            	</table>
            `
            document.getElementById('order-list').innerHTML = table
        }
    })
}


if (/admin/.test(window.location.href) && /single.html/.test(window.location.href)){

	var uri = window.location.href
	var url = new URL(uri)
	var order_id = url.searchParams.get("order")
	
	fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels/"+order_id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'token': localStorage.getItem('token')
        }
    })
    .then(res => res.json())
    .then(function(data){
        error = document.getElementById('error-meso')
        if (data['status'] == 'failure'){
            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
            error.style.display = "block";
        }else{
        	var single = `
        		<p id="error-meso"></p>
        		<img src="../../static/img/parcel.png" />
	            <div class="abt-cont">
	        `
	        single += "<p><strong>status : </strong> <small id='status'>"+data['data']['order_status']+"</small></p>"
	        single += "<p><strong>Pickup : </strong> <small>"+data['data']['pickup']+"</small></p>"
	        single += "<p><strong>Present : </strong> <small id='present'>"+data['data']['present']+"</small></p>"
	        single += "<p><strong>Destination : </strong> <small id='area'>"+data['data']['destination']+"</small></p>"
			single += "<p>"+data['data']['description']+"</p>"
	        single += `
	                <p class="text">
	                    <button onclick="changedesination()" class="success">Change Status</button>
	                    <button onclick="changelocation()" class="blue">Change Location</button>
	                </p>
	            </div>
        	`
        	document.getElementById('single-order').innerHTML = single
        	setTimeout(function(){
	            error.style.display = "none";
	        }, 3000)
        }
    })
}

function change_status(){
	error = document.getElementById('error-meso')
	if (document.getElementById("order-status").value != ''){
		var uri = window.location.href
		var url = new URL(uri)
		var order_id = url.searchParams.get("order")

		payload = {
			data: document.getElementById("order-status").value
		}
		
		fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels/"+order_id+"/status", {
	        method: 'PUT',
	        headers: {
	            'Content-Type': 'application/json',
	            'Accept': 'application/json',
	            'token': localStorage.getItem('token')
	        },
	        body: JSON.stringify(payload)
	    })
	    .then(res => res.json())
	    .then(function(data){
	        if (data['status'] == 'failure'){
	            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
	            error.style.background = "#dc3545";
	            error.style.display = "block";
	        }else{
	        	error.innerHTML = "<strong>Info! </strong> order status successfully changed";
	        	error.style.background = "#16a085";
	            error.style.display = "block";
	        	document.getElementById('status').innerHTML = document.getElementById("order-status").value
	        }
	    })
	    lgn.style.display = "none";
	}else{
		error.innerHTML = "<strong>Error! </strong> status cannot be empty.";
	    error.style.display = "block";
	    lgn.style.display = "none";
	}
	setTimeout(function(){
        error.style.display = "none";
    }, 3000)
}

function change_present_location(){
	error = document.getElementById('error-meso')
	if (document.getElementById("present-location").value != ''){
		var uri = window.location.href
		var url = new URL(uri)
		var order_id = url.searchParams.get("order")

		payload = {
			data: document.getElementById("present-location").value
		}
		
		fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels/"+order_id+"/presentLocation", {
	        method: 'PUT',
	        headers: {
	            'Content-Type': 'application/json',
	            'Accept': 'application/json',
	            'token': localStorage.getItem('token')
	        },
	        body: JSON.stringify(payload)
	    })
	    .then(res => res.json())
	    .then(function(data){
	        if (data['status'] == 'failure'){
	            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
	            error.style.background = "#dc3545";
	            error.style.display = "block";
	        }else{
	        	error.innerHTML = "<strong>Info! </strong> present location successfully changed";
	        	error.style.background = "#16a085";
	            error.style.display = "block";
	        	document.getElementById('present').innerHTML = document.getElementById("present-location").value
	        }
	    })
	    sgn.style.display = "none";
	}else{
		error.innerHTML = "<strong>Error! </strong> status cannot be empty.";
	    error.style.display = "block";
	    sgn.style.display = "none";
	}

	setTimeout(function(){
        error.style.display = "none";
    }, 3000)
}

if (/user/.test(window.location.href) && /profile.html/.test(window.location.href)){
	error = document.getElementById('error-meso')
	fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/users/", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'token': localStorage.getItem('token')
        }
    })
    .then(res => res.json())
	.then(function(data){
		if (data['status'] == 'failure'){
            error.innerHTML = "<strong>Error! </strong> " + data['error']['message'];
            error.style.background = "#dc3545";
            error.style.display = "block";
        }else{
        	document.getElementById('profile-username').innerHTML = data['data']['username']
        	document.getElementById('profile-fullname').innerHTML = (data['data']['firstname'] + " " + data['data']['lastname'])
        	document.getElementById('profile-contact').innerHTML = data['data']['contact']
        	document.getElementById('profile-email').innerHTML = data['data']['email']
        }
	})

	fetch("https://bagzie-send-it-final.herokuapp.com/api/v2/parcels", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'token': localStorage.getItem('token')
        }
    })
    .then(res => res.json())
    .then(function(data){
        error = document.getElementById('error-meso')

        if (data['status'] == 'failure'){
            document.getElementById('user-pending-order').innerHTML = "000";
            document.getElementById('user-transit-order').innerHTML = "000";
            document.getElementById('user-delivered-order').innerHTML = "000";
            document.getElementById('user-cancelled-order').innerHTML = "000";
        }else{
        	console.log(data['data'])
        	var pending = new Array()
        	var transit = new Array()
        	var delivered = new Array()
        	var cancelled = new Array()

        	for(var i=0; i < (data['data']).length; i++){
        		if(data['data'][i]['order_status'] == 'pending'){
        			pending.push(data['data'][i]['product'])
        		}

        		if(data['data'][i]['order_status'] == 'in-transit'){
        			transit.push(data['data'][i]['product'])
        		}

        		if(data['data'][i]['order_status'] == 'delivered'){
        			delivered.push(data['data'][i]['product'])
        		}

        		if(data['data'][i]['order_status'] == 'cancelled'){
        			cancelled.push(data['data'][i]['product'])
        		}
        	}

        	document.getElementById('user-pending-order').innerHTML = "00" + (pending.length);
            document.getElementById('user-transit-order').innerHTML = "00" + (transit.length);
            document.getElementById('user-delivered-order').innerHTML = "00" + (delivered.length);
            document.getElementById('user-cancelled-order').innerHTML = "00" + (cancelled.length);
        }
    })

	setTimeout(function(){
        error.style.display = "none";
    }, 3000)
}

//logout
function logout(){
	localStorage.removeItem('timer')
	localStorage.removeItem('token')
	localStorage.removeItem('usertype')
	window.location.href = '../../index.html'
}

//set time counter
setInterval(function(){
	var loginTime = localStorage.getItem('timer')
	var now = new Date().getTime();

	var remainingTime = (1000 * 60 * 30) - (now - loginTime);
	var minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60))
	var seconds = Math.floor((remainingTime % (1000 * 60)) / 1000)
	var sec = 0;

	if(seconds > 9){
		sec = seconds
	}else{
		sec = ("0" + seconds)
	}

	if (remainingTime <= 0) {
		logout()
	}else{
		document.getElementById('time-value').innerHTML = (minutes + ":" + sec)
	}
}, 1000)