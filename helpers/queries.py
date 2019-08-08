queries = {
  0 : """ SELECT id,merchantID,sellerName,shopName,
          email,password,status,storeAddress,city,country,
          contactNumber,storeDescription,zipcode,storeDetails,
          storePolicies,paymentMethod,DATE(syscreated) syscreated,sysmodified from `mlshop`.`merchantlist`;""",
  1 : "UPDATE `mlshop`.`merchantlist` SET status = 3 WHERE merchantID = %s AND email = %s;",
  2 : "UPDATE `mlshop`.`merchantlist`  SET  sellerName = %s,shopName= %s, email = %s, storeAddress = %s, city = %s, country  = %s, contactNumber = %s ,storeDescription = %s WHERE merchantID = %s",
  3 : """SELECT merchantID,sellerName,shopName,email,password,status,storeAddress,city,country,contactNumber,storeDescription,zipcode,storeDetails,storePolicies,paymentMethod,syscreated,sysmodified
       from `mlshop`.`merchantlist` WHERE merchantID = %s ;""",
  4 : "UPDATE `mlshop`.`merchantlist` SET status = 2 WHERE merchantID = %s AND email = %s;",
  5 : "SELECT * FROM `mlshop`.`Admin` WHERE email = %s AND password = %s AND `status`=1;",
  6 : "SELECT * FROM `mlshop`.`merchantlist` WHERE sellerName LIKE %s;",
  7 : "UPDATE `mlshop`.`merchantlist` SET `status` = 1 WHERE merchantID = %s AND email = %s;",
  8 : "UPDATE `mlshop`.`merchantlist` SET  `password` = %s WHERE merchantID = %s AND email = %s;",
  9 : "INSERT INTO %s(session_key,isExpired,expiration,created_at,updated_at) VALUES(%s,0,(SELECT DATE_ADD(NOW(),INTERVAL 1 HOUR)),NOW(),NOW());",
  10 : "UPDATE %s SET isExpired = 1 WHERE session_key = %s",
  11 : "SELECT NOW() as `date`",
  12 : "SELECT * from `mlshop`.`merchantlist`;"

}


def Query(qryNum:int) -> str :
    try:
      return queries[qryNum]
    except KeyError as e:
      return queries[0]




