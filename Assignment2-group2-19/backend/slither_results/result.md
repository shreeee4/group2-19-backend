Installing solc '0.8.4'...
Version '0.8.4' installed.
Switched global version to 0.8.4
Command slither Sample.sol --checklist failed with error:
'solc --version' running
'solc Sample.sol --combined-json abi,ast,bin,bin-runtime,srcmap,srcmap-runtime,userdoc,devdoc,hashes,compact-format --allow-paths .,C:\Users\DELL\Desktop\Semester 4\COS30049\Assignment2-group2-19\backend' running
Compilation warnings/errors on Sample.sol:
Warning: SPDX license identifier not provided in source file. Before publishing, consider adding a comment containing "SPDX-License-Identifier: <SPDX-License>" to each source file. Use "SPDX-License-Identifier: UNLICENSED" for non-open-source code. Please see https://spdx.org for more information.

--> Sample.sol



Warning: Unnamed return variable can remain unassigned. Add an explicit return with value to all non-reverting code paths or name the variable.

   --> Sample.sol:323:30:

    |

323 |     ) internal view returns (bytes memory) {

    |                              ^^^^^^^^^^^^



Warning: Unnamed return variable can remain unassigned. Add an explicit return with value to all non-reverting code paths or name the variable.

   --> Sample.sol:346:30:

    |

346 |     ) internal pure returns (bytes memory) {

    |                              ^^^^^^^^^^^^



Warning: Contract code size exceeds 24576 bytes (a limit introduced in Spurious Dragon). This contract may not be deployable on mainnet. Consider enabling the optimizer (with a low "runs" value!), turning off revert strings, or using libraries.

    --> Sample.sol:1103:1:

     |

1103 | contract HoldEarn is Operator {

     | ^ (Relevant source part starts here and spans across multiple lines).




INFO:Detectors:
HoldEarn._transferOut(address,address,uint256) (Sample.sol#2014-2022) sends eth to arbitrary user
	Dangerous calls:
	- address(user).transfer(amount) (Sample.sol#2019)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#functions-that-send-ether-to-arbitrary-destinations
INFO:Detectors:
Reentrancy in HoldEarn._getReward(uint256) (Sample.sol#1669-1708):
	External calls:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- userBet[msg.sender][pID].sTid.push(tID) (Sample.sol#1679)
	HoldEarn.userBet (Sample.sol#1196) can be used in cross function reentrancies:
	- HoldEarn._getReward(uint256) (Sample.sol#1669-1708)
	- HoldEarn.checkClaim(address,uint256) (Sample.sol#1574-1579)
	- HoldEarn.dealArray(uint256,uint256,address[]) (Sample.sol#1740-1766)
	- HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475)
	- HoldEarn.getUser(uint256,uint256) (Sample.sol#1825-1828)
	- HoldEarn.getUserBet(address,uint256) (Sample.sol#1894-1896)
	- HoldEarn.getUserReward(address,uint256,uint256) (Sample.sol#1638-1667)
	- HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614)
	- userReward[msg.sender][pID][tID].claimSort = sReward (Sample.sol#1678)
	HoldEarn.userReward (Sample.sol#1184) can be used in cross function reentrancies:
	- HoldEarn._getReward(uint256) (Sample.sol#1669-1708)
	- HoldEarn.userReward (Sample.sol#1184)
Reentrancy in HoldEarn._getReward(uint256) (Sample.sol#1669-1708):
	External calls:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID_scope_0].rewardToken,bReward) (Sample.sol#1693)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID_scope_0].rewardToken,bReward) (Sample.sol#1693)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- j < rewardID[pID].length() (Sample.sol#1687)
	HoldEarn.userBet (Sample.sol#1196) can be used in cross function reentrancies:
	- HoldEarn._getReward(uint256) (Sample.sol#1669-1708)
	- HoldEarn.checkClaim(address,uint256) (Sample.sol#1574-1579)
	- HoldEarn.dealArray(uint256,uint256,address[]) (Sample.sol#1740-1766)
	- HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475)
	- HoldEarn.getUser(uint256,uint256) (Sample.sol#1825-1828)
	- HoldEarn.getUserBet(address,uint256) (Sample.sol#1894-1896)
	- HoldEarn.getUserReward(address,uint256,uint256) (Sample.sol#1638-1667)
	- HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614)
	- userBet[msg.sender][pID].bTid.push(tID_scope_0) (Sample.sol#1691)
	HoldEarn.userBet (Sample.sol#1196) can be used in cross function reentrancies:
	- HoldEarn._getReward(uint256) (Sample.sol#1669-1708)
	- HoldEarn.checkClaim(address,uint256) (Sample.sol#1574-1579)
	- HoldEarn.dealArray(uint256,uint256,address[]) (Sample.sol#1740-1766)
	- HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475)
	- HoldEarn.getUser(uint256,uint256) (Sample.sol#1825-1828)
	- HoldEarn.getUserBet(address,uint256) (Sample.sol#1894-1896)
	- HoldEarn.getUserReward(address,uint256,uint256) (Sample.sol#1638-1667)
	- HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614)
	- userReward[msg.sender][pID][tID_scope_0].claimBase = bReward (Sample.sol#1690)
	HoldEarn.userReward (Sample.sol#1184) can be used in cross function reentrancies:
	- HoldEarn._getReward(uint256) (Sample.sol#1669-1708)
	- HoldEarn.userReward (Sample.sol#1184)
Reentrancy in HoldEarn.setDefaultToken(uint256,address,uint256) (Sample.sol#1392-1406):
	External calls:
	- _transferOut(msg.sender,periodInfo[pID].defaultToken,beforeAmount) (Sample.sol#1395)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferIn(msg.sender,token,afterAmount) (Sample.sol#1398)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransferFrom(user,address(this),amount) (Sample.sol#2026)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(msg.sender,periodInfo[pID].defaultToken,beforeAmount) (Sample.sol#1395)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferIn(msg.sender,token,afterAmount) (Sample.sol#1398)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- periodInfo[pID].defaultToken = token (Sample.sol#1403)
	HoldEarn.periodInfo (Sample.sol#1195) can be used in cross function reentrancies:
	- HoldEarn._getReward(uint256) (Sample.sol#1669-1708)
	- HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545)
	- HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440)
	- HoldEarn.check(address,uint256) (Sample.sol#1910-1914)
	- HoldEarn.checkAdd(address,uint256,HoldEarn.RewardTokenInfo) (Sample.sol#1916-1933)
	- HoldEarn.checkBase(address,uint256) (Sample.sol#1227-1234)
	- HoldEarn.checkDefault(address,address,uint256,uint256) (Sample.sol#1995-2012)
	- HoldEarn.checkDeposit(address,uint256,uint256) (Sample.sol#1769-1781)
	- HoldEarn.checkSetMinNum(address,uint256,uint256) (Sample.sol#1617-1636)
	- HoldEarn.checkSetRewardToken(address,address,uint256,uint256,uint256,uint256) (Sample.sol#1935-1958)
	- HoldEarn.checkWithdraw(address,uint256) (Sample.sol#2030-2051)
	- HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475)
	- HoldEarn.getPoolInfo(uint256) (Sample.sol#1860-1862)
	- HoldEarn.getStatus(uint256) (Sample.sol#1864-1892)
	- HoldEarn.getUserReward(address,uint256,uint256) (Sample.sol#1638-1667)
	- HoldEarn.notStart(uint256) (Sample.sol#1215-1218)
	- HoldEarn.setDefaultToken(uint256,address,uint256) (Sample.sol#1392-1406)
	- HoldEarn.setLockTime(uint256,uint256) (Sample.sol#1381-1390)
	- HoldEarn.setMinNum(uint256,uint256) (Sample.sol#1251-1254)
	- HoldEarn.setName(uint256,string) (Sample.sol#1220-1225)
	- HoldEarn.setPeriodTime(uint256,uint256) (Sample.sol#1370-1379)
	- HoldEarn.setUserNum(uint256,uint256,uint256) (Sample.sol#1257-1265)
	- HoldEarn.setUserToken(address,uint256,uint256) (Sample.sol#1267-1274)
	- HoldEarn.update(uint256) (Sample.sol#1477-1504)
	- HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614)
	- periodInfo[pID].perDefaultAmount = perAmount (Sample.sol#1404)
	HoldEarn.periodInfo (Sample.sol#1195) can be used in cross function reentrancies:
	- HoldEarn._getReward(uint256) (Sample.sol#1669-1708)
	- HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545)
	- HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440)
	- HoldEarn.check(address,uint256) (Sample.sol#1910-1914)
	- HoldEarn.checkAdd(address,uint256,HoldEarn.RewardTokenInfo) (Sample.sol#1916-1933)
	- HoldEarn.checkBase(address,uint256) (Sample.sol#1227-1234)
	- HoldEarn.checkDefault(address,address,uint256,uint256) (Sample.sol#1995-2012)
	- HoldEarn.checkDeposit(address,uint256,uint256) (Sample.sol#1769-1781)
	- HoldEarn.checkSetMinNum(address,uint256,uint256) (Sample.sol#1617-1636)
	- HoldEarn.checkSetRewardToken(address,address,uint256,uint256,uint256,uint256) (Sample.sol#1935-1958)
	- HoldEarn.checkWithdraw(address,uint256) (Sample.sol#2030-2051)
	- HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475)
	- HoldEarn.getPoolInfo(uint256) (Sample.sol#1860-1862)
	- HoldEarn.getStatus(uint256) (Sample.sol#1864-1892)
	- HoldEarn.getUserReward(address,uint256,uint256) (Sample.sol#1638-1667)
	- HoldEarn.notStart(uint256) (Sample.sol#1215-1218)
	- HoldEarn.setDefaultToken(uint256,address,uint256) (Sample.sol#1392-1406)
	- HoldEarn.setLockTime(uint256,uint256) (Sample.sol#1381-1390)
	- HoldEarn.setMinNum(uint256,uint256) (Sample.sol#1251-1254)
	- HoldEarn.setName(uint256,string) (Sample.sol#1220-1225)
	- HoldEarn.setPeriodTime(uint256,uint256) (Sample.sol#1370-1379)
	- HoldEarn.setUserNum(uint256,uint256,uint256) (Sample.sol#1257-1265)
	- HoldEarn.setUserToken(address,uint256,uint256) (Sample.sol#1267-1274)
	- HoldEarn.update(uint256) (Sample.sol#1477-1504)
	- HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614)
	- periodState[pID].totalDefaultAmount = afterAmount (Sample.sol#1405)
	HoldEarn.periodState (Sample.sol#1194) can be used in cross function reentrancies:
	- HoldEarn._getReward(uint256) (Sample.sol#1669-1708)
	- HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545)
	- HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440)
	- HoldEarn.checkClaim(address,uint256) (Sample.sol#1574-1579)
	- HoldEarn.checkDefault(address,address,uint256,uint256) (Sample.sol#1995-2012)
	- HoldEarn.checkDeposit(address,uint256,uint256) (Sample.sol#1769-1781)
	- HoldEarn.checkSetMinNum(address,uint256,uint256) (Sample.sol#1617-1636)
	- HoldEarn.checkSort(address,uint256,uint256,address[]) (Sample.sol#1711-1738)
	- HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475)
	- HoldEarn.getStatus(uint256) (Sample.sol#1864-1892)
	- HoldEarn.getUserReward(address,uint256,uint256) (Sample.sol#1638-1667)
	- HoldEarn.periodState (Sample.sol#1194)
	- HoldEarn.setDefaultToken(uint256,address,uint256) (Sample.sol#1392-1406)
	- HoldEarn.sortAccounts(uint256,uint256,address[]) (Sample.sol#1547-1567)
	- HoldEarn.update(uint256) (Sample.sol#1477-1504)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities
INFO:Detectors:
Reentrancy in HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440):
	External calls:
	- IERC20(rInfo[i].rewardToken).safeTransferFrom(msg.sender,address(this),rInfo[i].totalAmount) (Sample.sol#1427)
	State variables written after the call(s):
	- tID = ++ tokenInfoID[periodID] (Sample.sol#1418)
	HoldEarn.tokenInfoID (Sample.sol#1186) can be used in cross function reentrancies:
	- HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440)
	- HoldEarn.addToken(uint256,HoldEarn.RewardTokenInfo) (Sample.sol#1276-1300)
	- HoldEarn.tokenInfoID (Sample.sol#1186)
Reentrancy in HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475):
	External calls:
	- IERC20(periodInfo[pID].userToken).safeTransferFrom(msg.sender,address(this),amount) (Sample.sol#1461)
	State variables written after the call(s):
	- periodState[pID].totalAmount = periodState[pID].totalAmount.add(amount) (Sample.sol#1463)
	HoldEarn.periodState (Sample.sol#1194) can be used in cross function reentrancies:
	- HoldEarn._getReward(uint256) (Sample.sol#1669-1708)
	- HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545)
	- HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440)
	- HoldEarn.checkClaim(address,uint256) (Sample.sol#1574-1579)
	- HoldEarn.checkDefault(address,address,uint256,uint256) (Sample.sol#1995-2012)
	- HoldEarn.checkDeposit(address,uint256,uint256) (Sample.sol#1769-1781)
	- HoldEarn.checkSetMinNum(address,uint256,uint256) (Sample.sol#1617-1636)
	- HoldEarn.checkSort(address,uint256,uint256,address[]) (Sample.sol#1711-1738)
	- HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475)
	- HoldEarn.getStatus(uint256) (Sample.sol#1864-1892)
	- HoldEarn.getUserReward(address,uint256,uint256) (Sample.sol#1638-1667)
	- HoldEarn.periodState (Sample.sol#1194)
	- HoldEarn.setDefaultToken(uint256,address,uint256) (Sample.sol#1392-1406)
	- HoldEarn.sortAccounts(uint256,uint256,address[]) (Sample.sol#1547-1567)
	- HoldEarn.update(uint256) (Sample.sol#1477-1504)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities-1
INFO:Detectors:
HoldEarn.setRewardToken(uint256,uint256,address,uint256,uint256).tType (Sample.sol#1357) is a local variable never initialized
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#uninitialized-local-variables
INFO:Detectors:
HoldEarn.addToken(uint256,HoldEarn.RewardTokenInfo) (Sample.sol#1276-1300) ignores return value by sortID[pID].add(tID) (Sample.sol#1289)
HoldEarn.addToken(uint256,HoldEarn.RewardTokenInfo) (Sample.sol#1276-1300) ignores return value by rewardID[pID].add(tID) (Sample.sol#1292)
HoldEarn.removeToken(uint256,uint256) (Sample.sol#1302-1319) ignores return value by removeID[pID].add(tID) (Sample.sol#1305)
HoldEarn.removeToken(uint256,uint256) (Sample.sol#1302-1319) ignores return value by sortID[pID].remove(tID) (Sample.sol#1307)
HoldEarn.removeToken(uint256,uint256) (Sample.sol#1302-1319) ignores return value by rewardID[pID].remove(tID) (Sample.sol#1309)
HoldEarn.setRewardToken(uint256,uint256,address,uint256,uint256) (Sample.sol#1321-1368) ignores return value by rewardID[pID].remove(tID) (Sample.sol#1336)
HoldEarn.setRewardToken(uint256,uint256,address,uint256,uint256) (Sample.sol#1321-1368) ignores return value by sortID[pID].add(tID) (Sample.sol#1337)
HoldEarn.setRewardToken(uint256,uint256,address,uint256,uint256) (Sample.sol#1321-1368) ignores return value by sortID[pID].remove(tID) (Sample.sol#1339)
HoldEarn.setRewardToken(uint256,uint256,address,uint256,uint256) (Sample.sol#1321-1368) ignores return value by rewardID[pID].add(tID) (Sample.sol#1340)
HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440) ignores return value by sortID[periodID].add(tID) (Sample.sol#1422)
HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440) ignores return value by rewardID[periodID].add(tID) (Sample.sol#1424)
HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475) ignores return value by users[pID].add(msg.sender) (Sample.sol#1465)
HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475) ignores return value by remainDid[msg.sender][pID].add(id) (Sample.sol#1471)
HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614) ignores return value by hasClaimDid[msg.sender][pID].add(dID) (Sample.sol#1595)
HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614) ignores return value by remainDid[msg.sender][pID].remove(remainDid[msg.sender][pID].at(0)) (Sample.sol#1605)
HoldEarn.dealArray(uint256,uint256,address[]) (Sample.sol#1740-1766) ignores return value by sortUsers[pID][tID].add(user) (Sample.sol#1759)
HoldEarn.dealArray(uint256,uint256,address[]) (Sample.sol#1740-1766) ignores return value by sortUsers[pID][tID].add(user) (Sample.sol#1763)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#unused-return
INFO:Detectors:
Operator.setOperator(address) (Sample.sol#1088-1090) should emit an event for: 
	- operator = operator_ (Sample.sol#1089) 
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#missing-events-access-control
INFO:Detectors:
Operator.setOperator(address).operator_ (Sample.sol#1088) lacks a zero-check on :
		- operator = operator_ (Sample.sol#1089)
HoldEarn.setSortAccount(address).account (Sample.sol#1246) lacks a zero-check on :
		- sortAccount = account (Sample.sol#1247)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#missing-zero-address-validation
INFO:Detectors:
Reentrancy in HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545):
	External calls:
	- _transferOut(proAddress,periodInfo[pID].defaultToken,periodState[pID].totalDefaultAmount) (Sample.sol#1512)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(proAddress,periodInfo[pID].defaultToken,periodState[pID].totalDefaultAmount) (Sample.sol#1512)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- rewardTokenInfo[pID][tID].perAmount = rewardTokenInfo[pID][tID].totalAmount.mul(muti).div(periodState[pID].totalAmount) (Sample.sol#1516)
Reentrancy in HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545):
	External calls:
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_1].rewardToken,rewardTokenInfo[pID][tID_scope_1].totalAmount) (Sample.sol#1523)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_1].rewardToken,rewardTokenInfo[pID][tID_scope_1].totalAmount) (Sample.sol#1523)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- returnRewardAmount[pID][tID_scope_1] = rewardTokenInfo[pID][tID_scope_1].totalAmount (Sample.sol#1522)
Reentrancy in HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545):
	External calls:
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_1].rewardToken,rewardTokenInfo[pID][tID_scope_1].totalAmount) (Sample.sol#1523)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_3].rewardToken,rewardTokenInfo[pID][tID_scope_3].totalAmount) (Sample.sol#1529)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_1].rewardToken,rewardTokenInfo[pID][tID_scope_1].totalAmount) (Sample.sol#1523)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_3].rewardToken,rewardTokenInfo[pID][tID_scope_3].totalAmount) (Sample.sol#1529)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- returnDefaultAmount[pID] = periodState[pID].totalDefaultAmount (Sample.sol#1534)
	- returnDefaultAmount[pID] = value (Sample.sol#1540)
	- returnRewardAmount[pID][tID_scope_3] = rewardTokenInfo[pID][tID_scope_3].totalAmount (Sample.sol#1528)
Reentrancy in HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440):
	External calls:
	- IERC20(rInfo[i].rewardToken).safeTransferFrom(msg.sender,address(this),rInfo[i].totalAmount) (Sample.sol#1427)
	State variables written after the call(s):
	- periodState[periodID].totalDefaultAmount = amount (Sample.sol#1433)
	- rewardTokenInfo[periodID][tID] = rInfo[i] (Sample.sol#1419)
Reentrancy in HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475):
	External calls:
	- IERC20(periodInfo[pID].userToken).safeTransferFrom(msg.sender,address(this),amount) (Sample.sol#1461)
	State variables written after the call(s):
	- userBet[msg.sender][pID].totalAmount = userBet[msg.sender][pID].totalAmount.add(amount) (Sample.sol#1467)
	- id = ++ userBet[msg.sender][pID].dID (Sample.sol#1468)
	- userInfo[msg.sender][pID][id].amount = amount (Sample.sol#1469)
	- userInfo[msg.sender][pID][id].depositTime = block.timestamp (Sample.sol#1470)
Reentrancy in HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475):
	External calls:
	- IERC20(periodInfo[pID].userToken).safeTransferFrom(msg.sender,address(this),amount) (Sample.sol#1461)
	- update(pID) (Sample.sol#1473)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- update(pID) (Sample.sol#1473)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- update(pID) (Sample.sol#1473)
		- returnDefaultAmount[pID] = periodState[pID].totalDefaultAmount (Sample.sol#1511)
		- returnDefaultAmount[pID] = periodState[pID].totalDefaultAmount (Sample.sol#1534)
		- returnDefaultAmount[pID] = value (Sample.sol#1540)
	- update(pID) (Sample.sol#1473)
		- returnRewardAmount[pID][tID_scope_1] = rewardTokenInfo[pID][tID_scope_1].totalAmount (Sample.sol#1522)
		- returnRewardAmount[pID][tID_scope_3] = rewardTokenInfo[pID][tID_scope_3].totalAmount (Sample.sol#1528)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities-2
INFO:Detectors:
Reentrancy in HoldEarn._getReward(uint256) (Sample.sol#1669-1708):
	External calls:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- ClaimSortReward(msg.sender,rewardTokenInfo[pID][tID].rewardToken,pID,tID,sReward) (Sample.sol#1682)
Reentrancy in HoldEarn._getReward(uint256) (Sample.sol#1669-1708):
	External calls:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID_scope_0].rewardToken,bReward) (Sample.sol#1693)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID_scope_0].rewardToken,bReward) (Sample.sol#1693)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- ClaimBaseReward(msg.sender,rewardTokenInfo[pID][tID_scope_0].rewardToken,pID,tID_scope_0,bReward) (Sample.sol#1695)
Reentrancy in HoldEarn._getReward(uint256) (Sample.sol#1669-1708):
	External calls:
	- _transferOut(msg.sender,periodInfo[pID].defaultToken,periodInfo[pID].perDefaultAmount) (Sample.sol#1700)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(msg.sender,periodInfo[pID].defaultToken,periodInfo[pID].perDefaultAmount) (Sample.sol#1700)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- ClaimDefaultReward(msg.sender,periodInfo[pID].defaultToken,pID,periodInfo[pID].perDefaultAmount) (Sample.sol#1701)
Reentrancy in HoldEarn.addNewPeriod(HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1409-1440):
	External calls:
	- IERC20(rInfo[i].rewardToken).safeTransferFrom(msg.sender,address(this),rInfo[i].totalAmount) (Sample.sol#1427)
	- IERC20(newInfo.defaultToken).safeTransferFrom(msg.sender,address(this),amount) (Sample.sol#1435)
	Event emitted after the call(s):
	- AddNewPeriod(periodID) (Sample.sol#1439)
Reentrancy in HoldEarn.addToken(uint256,HoldEarn.RewardTokenInfo) (Sample.sol#1276-1300):
	External calls:
	- IERC20(rInfo.rewardToken).safeTransferFrom(msg.sender,address(this),rInfo.totalAmount) (Sample.sol#1296)
	Event emitted after the call(s):
	- AddToken(rInfo.rewardToken,rInfo.totalAmount,pID,tID,tType) (Sample.sol#1299)
Reentrancy in HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475):
	External calls:
	- IERC20(periodInfo[pID].userToken).safeTransferFrom(msg.sender,address(this),amount) (Sample.sol#1461)
	- update(pID) (Sample.sol#1473)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- update(pID) (Sample.sol#1473)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- Deposit(msg.sender,periodInfo[pID].userToken,pID,id,amount,userInfo[msg.sender][pID][id].depositTime) (Sample.sol#1474)
	- PeriodUpdate(pID) (Sample.sol#1493)
		- update(pID) (Sample.sol#1473)
	- PeriodUpdate(pID) (Sample.sol#1501)
		- update(pID) (Sample.sol#1473)
Reentrancy in HoldEarn.removeToken(uint256,uint256) (Sample.sol#1302-1319):
	External calls:
	- IERC20(rewardTokenInfo[pID][tID].rewardToken).safeTransfer(msg.sender,rewardTokenInfo[pID][tID].totalAmount) (Sample.sol#1313)
	External calls sending eth:
	- address(msg.sender).transfer(rewardTokenInfo[pID][tID].totalAmount) (Sample.sol#1315)
	Event emitted after the call(s):
	- RemoveToken(rewardTokenInfo[pID][tID].rewardToken,rewardTokenInfo[pID][tID].totalAmount,pID,tID) (Sample.sol#1318)
Reentrancy in HoldEarn.setRewardToken(uint256,uint256,address,uint256,uint256) (Sample.sol#1321-1368):
	External calls:
	- _transferOut(msg.sender,rToken,amount) (Sample.sol#1349)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- IERC20(token).safeTransferFrom(msg.sender,address(this),tokenAmount) (Sample.sol#1354)
	External calls sending eth:
	- _transferOut(msg.sender,rToken,amount) (Sample.sol#1349)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- ChangeToken(pID,tID,rToken,token,amount,tokenAmount,tType) (Sample.sol#1365)
Reentrancy in HoldEarn.transferTo(address,address,uint256) (Sample.sol#1442-1454):
	External calls:
	- IERC20(token).safeTransfer(account,amount) (Sample.sol#1447)
	External calls sending eth:
	- address(account).transfer(amount) (Sample.sol#1450)
	Event emitted after the call(s):
	- TransferTo(address(token),account,amount) (Sample.sol#1453)
Reentrancy in HoldEarn.update(uint256) (Sample.sol#1477-1504):
	External calls:
	- _periodPrize(pID,true) (Sample.sol#1491)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _periodPrize(pID,true) (Sample.sol#1491)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- PeriodUpdate(pID) (Sample.sol#1493)
Reentrancy in HoldEarn.update(uint256) (Sample.sol#1477-1504):
	External calls:
	- _periodPrize(pID,false) (Sample.sol#1499)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _periodPrize(pID,false) (Sample.sol#1499)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- PeriodUpdate(pID) (Sample.sol#1501)
Reentrancy in HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614):
	External calls:
	- _transferOut(msg.sender,periodInfo[pID].userToken,amount) (Sample.sol#1610)
		- returndata = address(token).functionCall(data,SafeERC20: low-level call failed) (Sample.sol#791)
		- IERC20(token).safeTransfer(user,amount) (Sample.sol#2017)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	External calls sending eth:
	- _transferOut(msg.sender,periodInfo[pID].userToken,amount) (Sample.sol#1610)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- WithdrawAll(msg.sender,pID,num,amount) (Sample.sol#1612)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities-3
INFO:Detectors:
HoldEarn.checkBase(address,uint256) (Sample.sol#1227-1234) uses timestamp for comparisons
	Dangerous comparisons:
	- require(bool,string)((user == owner() || user == operator) && 0 < pID && pID <= periodID && block.timestamp < periodInfo[pID].startTime,parama) (Sample.sol#1228-1233)
HoldEarn.update(uint256) (Sample.sol#1477-1504) uses timestamp for comparisons
	Dangerous comparisons:
	- users[pID].length() == periodInfo[pID].maxUserNum || (block.timestamp > time && users[pID].length() >= periodInfo[pID].minUserNum) (Sample.sol#1481-1482)
	- block.timestamp > time (Sample.sol#1484)
	- users[pID].length() < periodInfo[pID].minUserNum && block.timestamp > time (Sample.sol#1495)
HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614) uses timestamp for comparisons
	Dangerous comparisons:
	- block.timestamp > userInfo[msg.sender][pID][dID].depositTime.add(periodInfo[pID].lockTime) (Sample.sol#1591-1592)
HoldEarn.checkSetMinNum(address,uint256,uint256) (Sample.sol#1617-1636) uses timestamp for comparisons
	Dangerous comparisons:
	- require(bool,string)(block.timestamp < periodInfo[pID].startTime.add(periodInfo[pID].periodTime) || periodState[pID].endTime != 0,has end) (Sample.sol#1623-1627)
HoldEarn.checkDeposit(address,uint256,uint256) (Sample.sol#1769-1781) uses timestamp for comparisons
	Dangerous comparisons:
	- require(bool,string)(block.timestamp >= periodInfo[pID].startTime && block.timestamp < periodInfo[pID].startTime.add(periodInfo[pID].periodTime) && periodState[pID].endTime == 0,time err) (Sample.sol#1772-1776)
HoldEarn.checkNewPeriod(address,HoldEarn.PeriodInfo,HoldEarn.RewardTokenInfo[]) (Sample.sol#1783-1819) uses timestamp for comparisons
	Dangerous comparisons:
	- require(bool,string)(newInfo.startTime > block.timestamp && newInfo.periodTime > 0 && newInfo.lockTime > 0,time err) (Sample.sol#1798)
HoldEarn.getStatus(uint256) (Sample.sol#1864-1892) uses timestamp for comparisons
	Dangerous comparisons:
	- block.timestamp < periodInfo[pID].startTime (Sample.sol#1867)
	- periodInfo[pID].startTime <= block.timestamp && periodState[pID].endTime == 0 && block.timestamp < periodInfo[pID].startTime.add(periodInfo[pID].periodTime) (Sample.sol#1870-1872)
	- (periodState[pID].endTime != 0 && periodState[pID].endTime <= block.timestamp || block.timestamp >= periodInfo[pID].startTime.add(periodInfo[pID].periodTime)) && ! periodState[pID].isSort (Sample.sol#1876-1879)
	- periodState[pID].endTime != 0 && periodState[pID].endTime <= block.timestamp && periodState[pID].isSort (Sample.sol#1884-1886)
HoldEarn.check(address,uint256) (Sample.sol#1910-1914) uses timestamp for comparisons
	Dangerous comparisons:
	- require(bool,string)(block.timestamp < periodInfo[pID].startTime,has start) (Sample.sol#1913)
HoldEarn.checkWithdraw(address,uint256) (Sample.sol#2030-2051) uses timestamp for comparisons
	Dangerous comparisons:
	- require(bool,string)(block.timestamp > userInfo[user][pID][remainDid[user][pID].at(0)].depositTime.add(periodInfo[pID].lockTime) && ! userInfo[user][pID][remainDid[user][pID].at(0)].isClaim,no unLock) (Sample.sol#2044-2048)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#block-timestamp
INFO:Detectors:
Address._revert(bytes,string) (Sample.sol#354-366) uses assembly
	- INLINE ASM (Sample.sol#359-362)
EnumerableSet.values(EnumerableSet.AddressSet) (Sample.sol#613-623) uses assembly
	- INLINE ASM (Sample.sol#618-620)
EnumerableSet.values(EnumerableSet.UintSet) (Sample.sol#687-697) uses assembly
	- INLINE ASM (Sample.sol#692-694)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#assembly-usage
INFO:Detectors:
Address.functionCall(address,bytes) (Sample.sol#208-210) is never used and should be removed
Address.functionCallWithValue(address,bytes,uint256) (Sample.sol#237-243) is never used and should be removed
Address.functionDelegateCall(address,bytes) (Sample.sol#293-295) is never used and should be removed
Address.functionDelegateCall(address,bytes,string) (Sample.sol#303-310) is never used and should be removed
Address.functionStaticCall(address,bytes) (Sample.sol#268-270) is never used and should be removed
Address.functionStaticCall(address,bytes,string) (Sample.sol#278-285) is never used and should be removed
Address.sendValue(address,uint256) (Sample.sol#183-188) is never used and should be removed
Address.verifyCallResult(bool,bytes,string) (Sample.sol#342-352) is never used and should be removed
Context._msgData() (Sample.sol#1009-1011) is never used and should be removed
EnumerableSet._values(EnumerableSet.Set) (Sample.sol#481-483) is never used and should be removed
EnumerableSet.add(EnumerableSet.Bytes32Set,bytes32) (Sample.sol#497-499) is never used and should be removed
EnumerableSet.at(EnumerableSet.Bytes32Set,uint256) (Sample.sol#535-537) is never used and should be removed
EnumerableSet.contains(EnumerableSet.Bytes32Set,bytes32) (Sample.sol#514-516) is never used and should be removed
EnumerableSet.length(EnumerableSet.Bytes32Set) (Sample.sol#521-523) is never used and should be removed
EnumerableSet.remove(EnumerableSet.AddressSet,address) (Sample.sol#573-575) is never used and should be removed
EnumerableSet.remove(EnumerableSet.Bytes32Set,bytes32) (Sample.sol#507-509) is never used and should be removed
EnumerableSet.values(EnumerableSet.AddressSet) (Sample.sol#613-623) is never used and should be removed
EnumerableSet.values(EnumerableSet.Bytes32Set) (Sample.sol#547-549) is never used and should be removed
EnumerableSet.values(EnumerableSet.UintSet) (Sample.sol#687-697) is never used and should be removed
SafeERC20.safeApprove(IERC20,address,uint256) (Sample.sol#727-740) is never used and should be removed
SafeERC20.safeDecreaseAllowance(IERC20,address,uint256) (Sample.sol#751-762) is never used and should be removed
SafeERC20.safeIncreaseAllowance(IERC20,address,uint256) (Sample.sol#742-749) is never used and should be removed
SafeERC20.safePermit(IERC20Permit,address,address,uint256,uint256,uint8,bytes32,bytes32) (Sample.sol#764-778) is never used and should be removed
SafeMath.average(uint256,uint256) (Sample.sol#990-993) is never used and should be removed
SafeMath.bondingCurve(uint256,uint256) (Sample.sol#999-1001) is never used and should be removed
SafeMath.mod(uint256,uint256) (Sample.sol#928-930) is never used and should be removed
SafeMath.mod(uint256,uint256,string) (Sample.sol#944-951) is never used and should be removed
SafeMath.percentageAmount(uint256,uint8) (Sample.sol#970-972) is never used and should be removed
SafeMath.percentageOfTotal(uint256,uint256) (Sample.sol#981-983) is never used and should be removed
SafeMath.quadraticPricing(uint256,uint256) (Sample.sol#995-997) is never used and should be removed
SafeMath.sqrrt(uint256) (Sample.sol#954-965) is never used and should be removed
SafeMath.sub(uint256,uint256) (Sample.sol#827-829) is never used and should be removed
SafeMath.sub(uint256,uint256,string) (Sample.sol#841-850) is never used and should be removed
SafeMath.substractPercentage(uint256,uint8) (Sample.sol#977-979) is never used and should be removed
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#dead-code
INFO:Detectors:
Pragma version0.8.4 (Sample.sol#1) allows old versions
solc-0.8.4 is not recommended for deployment
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#incorrect-versions-of-solidity
INFO:Detectors:
Low level call in Address.sendValue(address,uint256) (Sample.sol#183-188):
	- (success) = recipient.call{value: amount}() (Sample.sol#186)
Low level call in Address.functionCallWithValue(address,bytes,uint256,string) (Sample.sol#251-260):
	- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
Low level call in Address.functionStaticCall(address,bytes,string) (Sample.sol#278-285):
	- (success,returndata) = target.staticcall(data) (Sample.sol#283)
Low level call in Address.functionDelegateCall(address,bytes,string) (Sample.sol#303-310):
	- (success,returndata) = target.delegatecall(data) (Sample.sol#308)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#low-level-calls
INFO:Detectors:
Function IERC20Permit.DOMAIN_SEPARATOR() (Sample.sol#129) is not in mixedCase
Constant Operator.baseRate (Sample.sol#1081) is not in UPPER_CASE_WITH_UNDERSCORES
Constant HoldEarn.muti (Sample.sol#1123) is not in UPPER_CASE_WITH_UNDERSCORES
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#conformance-to-solidity-naming-conventions
INFO:Detectors:
Reentrancy in HoldEarn._getReward(uint256) (Sample.sol#1669-1708):
	External calls:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- userBet[msg.sender][pID].sTid.push(tID) (Sample.sol#1679)
	- userReward[msg.sender][pID][tID].claimSort = sReward (Sample.sol#1678)
	Event emitted after the call(s):
	- ClaimSortReward(msg.sender,rewardTokenInfo[pID][tID].rewardToken,pID,tID,sReward) (Sample.sol#1682)
Reentrancy in HoldEarn._getReward(uint256) (Sample.sol#1669-1708):
	External calls:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- address(user).transfer(amount) (Sample.sol#2019)
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID_scope_0].rewardToken,bReward) (Sample.sol#1693)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID].rewardToken,sReward) (Sample.sol#1681)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferOut(msg.sender,rewardTokenInfo[pID][tID_scope_0].rewardToken,bReward) (Sample.sol#1693)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- j < rewardID[pID].length() (Sample.sol#1687)
	- userBet[msg.sender][pID].bTid.push(tID_scope_0) (Sample.sol#1691)
	- userReward[msg.sender][pID][tID_scope_0].claimBase = bReward (Sample.sol#1690)
	Event emitted after the call(s):
	- ClaimBaseReward(msg.sender,rewardTokenInfo[pID][tID_scope_0].rewardToken,pID,tID_scope_0,bReward) (Sample.sol#1695)
Reentrancy in HoldEarn._getReward(uint256) (Sample.sol#1669-1708):
	External calls:
	- _transferOut(msg.sender,periodInfo[pID].defaultToken,periodInfo[pID].perDefaultAmount) (Sample.sol#1700)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _transferOut(msg.sender,periodInfo[pID].defaultToken,periodInfo[pID].perDefaultAmount) (Sample.sol#1700)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- ClaimDefaultReward(msg.sender,periodInfo[pID].defaultToken,pID,periodInfo[pID].perDefaultAmount) (Sample.sol#1701)
Reentrancy in HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545):
	External calls:
	- _transferOut(proAddress,periodInfo[pID].defaultToken,periodState[pID].totalDefaultAmount) (Sample.sol#1512)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _transferOut(proAddress,periodInfo[pID].defaultToken,periodState[pID].totalDefaultAmount) (Sample.sol#1512)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- rewardTokenInfo[pID][tID].perAmount = rewardTokenInfo[pID][tID].totalAmount.mul(muti).div(periodState[pID].totalAmount) (Sample.sol#1516)
Reentrancy in HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545):
	External calls:
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_1].rewardToken,rewardTokenInfo[pID][tID_scope_1].totalAmount) (Sample.sol#1523)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_1].rewardToken,rewardTokenInfo[pID][tID_scope_1].totalAmount) (Sample.sol#1523)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- returnRewardAmount[pID][tID_scope_1] = rewardTokenInfo[pID][tID_scope_1].totalAmount (Sample.sol#1522)
Reentrancy in HoldEarn._periodPrize(uint256,bool) (Sample.sol#1506-1545):
	External calls:
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_1].rewardToken,rewardTokenInfo[pID][tID_scope_1].totalAmount) (Sample.sol#1523)
		- address(user).transfer(amount) (Sample.sol#2019)
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_3].rewardToken,rewardTokenInfo[pID][tID_scope_3].totalAmount) (Sample.sol#1529)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_1].rewardToken,rewardTokenInfo[pID][tID_scope_1].totalAmount) (Sample.sol#1523)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferOut(proAddress,rewardTokenInfo[pID][tID_scope_3].rewardToken,rewardTokenInfo[pID][tID_scope_3].totalAmount) (Sample.sol#1529)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- returnDefaultAmount[pID] = periodState[pID].totalDefaultAmount (Sample.sol#1534)
	- returnDefaultAmount[pID] = value (Sample.sol#1540)
	- returnRewardAmount[pID][tID_scope_3] = rewardTokenInfo[pID][tID_scope_3].totalAmount (Sample.sol#1528)
Reentrancy in HoldEarn.deposit(uint256,uint256) (Sample.sol#1456-1475):
	External calls:
	- update(pID) (Sample.sol#1473)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- update(pID) (Sample.sol#1473)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- Deposit(msg.sender,periodInfo[pID].userToken,pID,id,amount,userInfo[msg.sender][pID][id].depositTime) (Sample.sol#1474)
Reentrancy in HoldEarn.removeToken(uint256,uint256) (Sample.sol#1302-1319):
	External calls:
	- address(msg.sender).transfer(rewardTokenInfo[pID][tID].totalAmount) (Sample.sol#1315)
	Event emitted after the call(s):
	- RemoveToken(rewardTokenInfo[pID][tID].rewardToken,rewardTokenInfo[pID][tID].totalAmount,pID,tID) (Sample.sol#1318)
Reentrancy in HoldEarn.setDefaultToken(uint256,address,uint256) (Sample.sol#1392-1406):
	External calls:
	- _transferOut(msg.sender,periodInfo[pID].defaultToken,beforeAmount) (Sample.sol#1395)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _transferOut(msg.sender,periodInfo[pID].defaultToken,beforeAmount) (Sample.sol#1395)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	- _transferIn(msg.sender,token,afterAmount) (Sample.sol#1398)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	State variables written after the call(s):
	- periodInfo[pID].defaultToken = token (Sample.sol#1403)
	- periodInfo[pID].perDefaultAmount = perAmount (Sample.sol#1404)
	- periodState[pID].totalDefaultAmount = afterAmount (Sample.sol#1405)
Reentrancy in HoldEarn.setRewardToken(uint256,uint256,address,uint256,uint256) (Sample.sol#1321-1368):
	External calls:
	- _transferOut(msg.sender,rToken,amount) (Sample.sol#1349)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _transferOut(msg.sender,rToken,amount) (Sample.sol#1349)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- ChangeToken(pID,tID,rToken,token,amount,tokenAmount,tType) (Sample.sol#1365)
Reentrancy in HoldEarn.transferTo(address,address,uint256) (Sample.sol#1442-1454):
	External calls:
	- address(account).transfer(amount) (Sample.sol#1450)
	Event emitted after the call(s):
	- TransferTo(address(token),account,amount) (Sample.sol#1453)
Reentrancy in HoldEarn.update(uint256) (Sample.sol#1477-1504):
	External calls:
	- _periodPrize(pID,true) (Sample.sol#1491)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _periodPrize(pID,true) (Sample.sol#1491)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- PeriodUpdate(pID) (Sample.sol#1493)
Reentrancy in HoldEarn.update(uint256) (Sample.sol#1477-1504):
	External calls:
	- _periodPrize(pID,false) (Sample.sol#1499)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _periodPrize(pID,false) (Sample.sol#1499)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- PeriodUpdate(pID) (Sample.sol#1501)
Reentrancy in HoldEarn.withdrawAll(uint256) (Sample.sol#1581-1614):
	External calls:
	- _transferOut(msg.sender,periodInfo[pID].userToken,amount) (Sample.sol#1610)
		- address(user).transfer(amount) (Sample.sol#2019)
	External calls sending eth:
	- _transferOut(msg.sender,periodInfo[pID].userToken,amount) (Sample.sol#1610)
		- address(user).transfer(amount) (Sample.sol#2019)
		- (success,returndata) = target.call{value: value}(data) (Sample.sol#258)
	Event emitted after the call(s):
	- WithdrawAll(msg.sender,pID,num,amount) (Sample.sol#1612)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#reentrancy-vulnerabilities-4
INFO:Detectors:
Variable HoldEarn._getReward(uint256).tID_scope_0 (Sample.sol#1688) is too similar to HoldEarn._periodPrize(uint256,bool).tID_scope_1 (Sample.sol#1521)
Variable HoldEarn._periodPrize(uint256,bool).tID_scope_1 (Sample.sol#1521) is too similar to HoldEarn._periodPrize(uint256,bool).tID_scope_3 (Sample.sol#1527)
Variable HoldEarn._getReward(uint256).tID_scope_0 (Sample.sol#1688) is too similar to HoldEarn._periodPrize(uint256,bool).tID_scope_3 (Sample.sol#1527)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#variable-names-too-similar
INFO:Detectors:
Operator.baseRate (Sample.sol#1081) is never used in HoldEarn (Sample.sol#1103-2052)
Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#unused-state-variable
INFO:Slither:Sample.sol analyzed (10 contracts with 88 detectors), 118 result(s) found
