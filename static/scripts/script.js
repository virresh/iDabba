new Vue({
	delimiters: ['${', '}'] ,
	el: '#stats',
	data: {
		iname:'',
		iTemp:'',
		iCount:'',
		iHumid:'',
		iWeight:''
	},	

	http: {
			emulateJSON: true,
			emulateHTTP: true
	},

	mounted: function() {
		this.iname = "Fetch Data. It will appear here.";
	},

	methods: {														
		itemname: function() {
			this.$http.get('/api/iname')
			.then(function (x) {
				this.iname = x.body['objectName'];
				//console.log(x);
			})
			.catch(function (err) {
				console.log(err);
			});
		}

		itemdata: function() {
			this.$http.get('/api/iname')
			.then(function (x) {
				this.iname = x.body['objectName'];
				//console.log(x);
			})
			.catch(function (err) {
				console.log(err);
			});
		}
	}
});