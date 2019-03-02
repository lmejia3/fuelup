angular.module("yoFeul")
    .controller("clientCtrl", function($scope) {
        $scope.model=[
            {gallons: 152, address: "fakeaddress_1", rdate: "fakeQuoteDate_1", ddate: "fakeRequestDate_1",price: 3284765,paid: false},
            {gallons: 1234, address: "fakeaddress_2", rdate: "fakeQuoteDate_2", ddate: "fakeRequestDate_2",price: 3281245,paid: true},
            {gallons: 6765, address: "fakeaddress_3", rdate: "fakeQuoteDate_3", ddate: "fakeRequestDate_3",price: 23455126,paid: true},
            {gallons: 234, address: "fakeaddress_4", rdate: "fakeQuoteDate_4", ddate: "fakeRequestDate_4",price: 1234543,paid: true},
            {gallons: 25783, address: "fakeaddress_5", rdate: "fakeQuoteDate_5", ddate: "fakeRequestDate_5",price: 3645324512,paid: true}
        ];

        $scope.setUsername = function(name){
            $scope.username=name;
        }
    })