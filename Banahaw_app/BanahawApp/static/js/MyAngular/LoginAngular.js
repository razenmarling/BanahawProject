'use strict';

var MyApp = angular.module("MyApp",[]);

MyApp.controller('MyController',['$scope','$window','Requests',function($scope,$window,Requests){
	$scope.user_data = null;
	$scope.username = '';
	$scope.password = '';
	$scope.status = false;
	$scope.msg = '';


	$scope.validate = function(user,pass){
		Requests.getValidation(user,pass).then(function(response){
			if (response.status = 'OK'){
				$scope.user_data = response.data;
				angular.forEach($scope.user_data.data,function(value,key){
					if($scope.user_data.status == 'OK'){
						$scope.msg = '';
						$scope.status = false;
						if(value.role == 'administrator'){
							$window.location.href = '/admin';
						}else{
							$window.location.href = '/user';
						};
						
					}else{
						$scope.status = true;
						$scope.msg = value.Message;
					};

				});

			};
		});
	};

	
}]);

MyApp.factory('Requests',function($http){
		return {
			getValidation:function(user,pass){
				return $http({
				method:'GET',
				url:'http://localhost:5000/login/validation'+'?username='+user+'&'+'password='+pass,
				});
			}
		}
});