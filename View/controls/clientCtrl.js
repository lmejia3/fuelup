angular.module("yoFeul")
    .controller("clientCtrl", function($scope) {
        $scope.model=[
            {gallons: 152, address: "fakeaddress_1", rdate: "fakeQuoteDate_1", ddate: "fakeRequestDate_1",price: 3284765,paid: false},
            {gallons: 1234, address: "fakeaddress_2", rdate: "fakeQuoteDate_2", ddate: "fakeRequestDate_2",price: 3281245,paid: true},
            {gallons: 6765, address: "fakeaddress_3", rdate: "fakeQuoteDate_3", ddate: "fakeRequestDate_3",price: 23455126,paid: true},
            {gallons: 234, address: "fakeaddress_4", rdate: "fakeQuoteDate_4", ddate: "fakeRequestDate_4",price: 1234543,paid: true},
            {gallons: 25783, address: "fakeaddress_5", rdate: "fakeQuoteDate_5", ddate: "fakeRequestDate_5",price: 3645324512,paid: true}
        ];

    })

var mod = angular.module("yoFeul")

mod.controller("loginCtrl", function($scope, loginService){
    this.login = function(user, pass){
        if(user == undefined){

        }
        if(pass == undefined){

        }
        
        var lg = loginService;
        var promise = lg.login(user, pass);

        promise.then(
            function (response) {
                console.log('successful responce');
                console.log(response);
                data = response.data;
                if('error' in data){
                    console.log(data.error)
                } else {
                    lg.username = user;
                    console.log("IM HERE: " + lg.username);
                    lg.password = pass;
                    lg.key = data.key
                    lg.loggedIn = true;
                    $scope.updateName();
                    window.location = '#!user/profile';
                }
            },
            function (response) {
                console.log('failed responce');
                console.log(response);
            }
        );
    }

});

mod.controller('registerCtrl', function($scope, registerService){
    this.register = function(user, pass, conf){
        if(user == undefined){

        }
        if(pass == undefined){
            
        }
        if(conf == undefined){
            
        }

        var rs = registerService;
        var promise = rs.register(user, pass, conf);
        
        promise.then(
            function (reponse){
                console.log('successful responce');
                console.log(response);
                data = response.data;
                if('error' in data){
                    console.log(data.error)
                } else{
                    console.log('registered');
                    window.location = '#!login';
                }
            },
            function (response){
                console.log('failed responce');
                console.log(response);
            }
        );
    };


});

