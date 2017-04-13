new Vue({
	delimiters: ['${', '}'] ,
	el: '#tabs',
	data: {
		iname:'',
		iTemp:'',
		iHumid:'',
		iWeight:'',
		rfidV:''
	},	

	http: {
			emulateJSON: true,
			emulateHTTP: true
	},

	mounted: function() {
		// this.iname = "Fetch Data. It will appear here.";
		this.itemdata();
	},

	methods: {														
		itemdata: function() {
			//console.log("Here");
			this.$http.get('/api/getrd')
			.then(function (x) {
				this.iname = x.body['objectName'];
				this.iTemp = x.body['temp'];
				this.iHumid = x.body['humidity'];
				this.iWeight = x.body['weight'];
				this.rfidV = x.body['rfid'];
				//console.log(x);
			})
			.catch(function (err) {
				console.log(err);
			});
		}
	}
});



//iCount:'',

// ,
//
// 		itemname: function() {
// 			this.$http.get('/api/getrd')
// 			.then(function (x) {
// 				this.iname = x.body['objectName'];
// 				//console.log(x);
// 			})
// 			.catch(function (err) {
// 				console.log(err);
// 			});
// 		}