queries = {
  0 : """ SELECT id,merchantID,sellerName,shopName,
          email,password,status,storeAddress,city,country,
          contactNumber,storeDescription,zipcode,storeDetails,
          storePolicies,paymentMethod,DATE(syscreated) syscreated,sysmodified from `mlshop`.`merchantlist`;""",
  1 : "UPDATE `mlshop`.`merchantlist` SET status = 3 WHERE merchantID = ? AND email = ?;",
  2 : "UPDATE `mlshop`.`merchantlist`  SET  sellerName = ?,shopName= ?, email = ?, storeAddress = ?, city = ?, country  = ?, contactNumber = ? ,storeDescription = ? WHERE merchantID = ?",
  3 : """SELECT merchantID,sellerName,shopName,email,password,status,storeAddress,city,country,contactNumber,storeDescription,zipcode,storeDetails,storePolicies,paymentMethod,syscreated,sysmodified
       from `mlshop`.`merchantlist` WHERE merchantID = ? ;"""
}


def Query(qryNum:int) -> str :
    try:
      return queries[qryNum]
    except KeyError as e:
      return queries[0]




