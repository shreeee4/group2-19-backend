def db_config_statements():
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "mypythondb"
    }
    return db_config

def database_structure():
    structure ={"CREATE TABLE IF NOT EXISTS Vulnerabilities ("
                "vulnerability_id INT PRIMARY KEY,"
                "vulnerability_name VARCHAR(255) NOT NULL,"
                "impact ENUM('High', 'Medium', 'Low') NOT NULL,"
                "description TEXT,"
                "recomendation TEXT"
                ");"
                "CREATE TABLE IF NOT EXISTS Reports ("
                "report_id INT AUTO_INCREMENT PRIMARY KEY,"
                "report_number INT,"
                "contract_name VARCHAR(255) NOT NULL,"
                "audit_date DATE NOT NULL"
                ");"
                "CREATE TABLE IF NOT EXISTS ReportVulnerabilities ("
                "report_vulnerability_id INT AUTO_INCREMENT PRIMARY KEY,"
                "report_id INT,"
                "vulnerability_id INT,"
                "FOREIGN KEY (report_id) REFERENCES Reports(report_id),"
                "FOREIGN KEY (vulnerability_id) REFERENCES Vulnerabilities(vulnerability_id)"
                ");"
                }
    return structure

def valnrabilaties_insert():
    valnrabilatieStatements ={"INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (1,'storage-abiencoderv2-array', 'High', 'solc versions 0.4.7-0.5.9 contain a compiler bug leading to incorrect ABI encoder usage.','Use a compiler >= 0.5.10.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (2,'arbitrary-from-in-transferfrom', 'High', 'Detect when msg.sender is not used as from in transferFrom.','Use msg.sender as from in transferFrom.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (3,'modifying-storage-array-by-value', 'High', 'Detect arrays passed to a function that expects reference to a storage array','Ensure the correct usage of memory and storage in the function parameters. Make all the locations explicit.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (4,'abi-encodepacked-collision', 'High', 'Detect collision due to dynamic type usages in abi.encodePacked','Do not use more than one dynamic type in abi.encodePacked() (see the Solidity documentation). Use abi.encode(), preferably.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (5,'incorrect-shift-in-assembly', 'High', 'Detect if the values in a shift operation are reversed','Swap the order of parameters.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (6,'multiple-constructor-schemes', 'High', 'Detect multiple constructor definitions in the same contract (using new and old schemes).','Only declare one constructor, preferably using the new scheme constructor(...) instead of function <contractName>(...).');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (7,'name-reused', 'High', 'If a codebase has two contracts the similar names, the compilation artifacts will not contain one of the contracts with the duplicate name.','Rename the contract.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (8,'protected-variables', 'High', 'Detect unprotected variable that are marked protected','Add access controls to the vulnerable function');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (9,'public-mappings-with-nested-variables', 'High', 'Prior to Solidity 0.5, a public mapping with nested structures returned incorrect values.','Do not use public mapping with nested structures.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (10,'right-to-left-override-character', 'High', 'An attacker can manipulate the logic of the contract by using a right-to-left-override character (U+202E).','Special control characters must not be allowed.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (11,'state-variable-shadowing', 'High', 'Detection of state variables shadowed.','Remove the state variable shadowing.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (12,'suicidal', 'High', 'Unprotected call to a function executing selfdestruct/suicide.','Protect access to all sensitive functions.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (13,'uninitialized-state-variables', 'High', 'Uninitialized state variables.','Initialize all the variables. If a variable is meant to be initialized to zero, explicitly set it to zero to improve code readability.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (14,'uninitialized-storage-variables','High', 'An uninitialized storage variable will act as a reference to the first state variable, and can override a critical variable.', 'Initialize all storage variables.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (15,'unprotected-upgradeable-contract', 'High', 'Detects logic contract that can be destructed.','Add a constructor to ensure initialize cannot be called on the logic contract.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (16,'arbitrary-from-in-transferfrom-used-with-permit', 'High', 'Detect when msg.sender is not used as from in transferFrom and permit is used.','Ensure that the underlying ERC20 token correctly implements a permit function.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (17,'functions-that-send-ether-to-arbitrary-destinations', 'High', 'Unprotected call to a function sending Ether to an arbitrary address.','Ensure that an arbitrary user cannot withdraw unauthorized funds.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (18,'array-length-assignment', 'High', 'Detects the direct assignment of an arrays length.','Do not allow array lengths to be set directly set; instead, opt to add values as needed. Otherwise, thoroughly review the contract to ensure a user-controlled variable cannot reach an array length assignment.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (19,'controlled-delegatecall', 'High', 'Delegatecall or callcode to an address controlled by the user.','Avoid using delegatecall. Use only trusted destinations.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (20,'payable-functions-using-delegatecall-inside-a-loop', 'High', 'Detect the use of delegatecall inside a loop in a payable function.','Carefully check that the function called by delegatecall is not payable/doesnt use msg.value.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (21,'msgvalue-inside-a-loop','High', 'Detect the use of msg.value inside a loop.', 'Provide an explicit array of amounts alongside the receivers array, and check that the sum of all amounts matches msg.value.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (22,'reentrancy-vulnerabilities', 'High', 'Detection of the reentrancy bug. Do not report reentrancies that dont involve Ether (see reentrancy-no-eth)','Apply the check-effects-interactions pattern.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (23,'storage-signed-integer-array','High', 'solc versions 0.4.7-0.5.9 contain a compiler bug leading to incorrect values in signed integer arrays.', 'Use a compiler version >= 0.5.10.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (24,'unchecked-transfer', 'High', 'The return value of an external transfer/transferFrom call is not checked','Use SafeERC20, or ensure that the transfer/transferFrom return value is checked.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (25,'weak-prng', 'High', 'Weak PRNG due to a modulo on block.timestamp, now or blockhash. These can be influenced by miners to some extent so they should be avoided.','Do not use block.timestamp, now or blockhash as a source of randomness');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (26,'codex', 'High', 'Use codex to find vulnerabilities','Review codexs message.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (27,'domain-separator-collision', 'Medium', 'An ERC20 token has a function whose signature collides with EIP-2612s DOMAIN_SEPARATOR(), causing unanticipated behavior for contracts using permit functionality.','Remove or rename the function that collides with DOMAIN_SEPARATOR().');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (28,'dangerous-enum-conversion', 'Medium', 'Detect out-of-range enum conversion (solc < 0.4.5).','Use a recent compiler version. If solc <0.4.5 is required, check the enum conversion range.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (29,'incorrect-erc20-interface', 'Medium', 'Incorrect return values for ERC20 functions. A contract compiled with Solidity > 0.4.22 interacting with these functions will fail to execute them, as the return value is missing.','Set the appropriate return values and types for the defined ERC20 functions.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (30,'incorrect-erc721-interface', 'Medium', 'Incorrect return values for ERC721 functions. A contract compiled with solidity > 0.4.22 interacting with these functions will fail to execute them, as the return value is missing.','Set the appropriate return values and vtypes for the defined ERC721 functions.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (31,'dangerous-strict-equalities', 'Medium', 'Use of strict equalities that can be easily manipulated by an attacker.','Dont use strict equality to determine if an account has enough Ether or tokens.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (32,'contracts-that-lock-ether', 'Medium', 'Contract with a payable function, but without a withdrawal capacity.','Remove the payable attribute or add a withdraw function.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (33,'deletion-on-mapping-containing-a-structure', 'Medium', 'A deletion in a structure containing a mapping will not delete the mapping (see the Solidity documentation). The remaining data may be used to compromise the contract.','Use a lock mechanism instead of a deletion to disable structure containing a mapping.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (34,'state-variable-shadowing-from-abstract-contracts', 'Medium', 'Detection of state variables shadowed from abstract contracts.','Remove the state variable shadowing.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (35,'tautology-or-contradiction', 'Medium', 'Detects expressions that are tautologies or contradictions.','Fix the incorrect comparison by changing the value type or the comparison.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (36,'write-after-write', 'Medium', 'Detects variables that are written but never read and written again.','Fix or remove the writes.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (37,'misuse-of-a-boolean-constant', 'Medium', 'Detects the misuse of a Boolean constant.','Verify and simplify the condition.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (38,'constant-functions-using-assembly-code', 'Medium', 'Functions declared as constant/pure/view using assembly code.constant/pure/view was not enforced prior to Solidity 0.5. Starting from Solidity 0.5, a call to a constant/pure/view function uses the STATICCALL opcode, which reverts in case of state modification. As a result, a call to an incorrectly labeled function may trap a contract compiled with Solidity 0.5.','Ensure the attributes of contracts compiled prior to Solidity 0.5.0 are correct.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (39,'constant-functions-changing-the-state', 'Medium', 'Functions declared as constant/pure/view change the state. constant/pure/view was not enforced prior to Solidity 0.5. Starting from Solidity 0.5, a call to a constant/pure/view function uses the STATICCALL opcode, which reverts in case of state modification. As a result, a call to an incorrectly labeled function may trap a contract compiled with Solidity 0.5.','Ensure that attributes of contracts compiled prior to Solidity 0.5.0 are correct.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (40,'divide-before-multiply', 'Medium', 'Soliditys integer division truncates. Thus, performing division before multiplication can lead to precision loss.','Consider ordering multiplication before division.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (41,'reentrancy-vulnerabilities-1', 'Medium', 'Detection of the reentrancy bug. Do not report reentrancies that involve Ether (see reentrancy-eth).','Apply the check-effects-interactions pattern.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (42,'reused-base-constructors', 'Medium', 'Detects if the same base constructor is called with arguments from two different locations in the same inheritance hierarchy.','Remove the duplicate constructor call.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (43,'dangerous-usage-of-txorigin', 'Medium', 'tx.origin-based protection can be abused by a malicious contract if a legitimate user interacts with the malicious contract.','Do not use tx.origin for authorization.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (44,'unchecked-low-level-calls', 'Medium', 'The return value of a low-level call is not checked.','Ensure that the return value of a low-level call is checked or logged.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (45,'unchecked-send', 'Medium', 'The return value of a send is not checked.','Ensure that the return value of send is checked or logged.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (46,'uninitialized-local-variables', 'Medium', 'Uninitialized local variables.','Initialize all the variables. If a variable is meant to be initialized to zero, explicitly set it to zero to improve code readability.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (47,'unused-return', 'Medium', 'The return value of an external call is not stored in a local or state variable.','Ensure that all the return values of the function calls are used.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (48,'incorrect-modifier', 'Low', 'If a modifier does not execute _ or revert, the execution of the function will return the default value, which can be misleading for the caller.','All the paths in a modifier must execute _ or revert.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (49,'builtin-symbol-shadowing', 'Low', 'Detection of shadowing built-in symbols using local variables, state variables, functions, modifiers, or events.','Rename the local variables, state variables, functions, modifiers, and events that shadow a builtin symbol.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (50,'local-variable-shadowing', 'Low', 'Detection of shadowing using local variables.','Rename the local variables that shadow another component.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (51,'uninitialized-function-pointers-in-constructors', 'Low', 'solc versions 0.4.5-0.4.26 and 0.5.0-0.5.8 contain a compiler bug leading to unexpected behavior when calling uninitialized function pointers in constructors.','Initialize function pointers before calling. Avoid function pointers if possible.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (52,'pre-declaration-usage-of-local-variables', 'Low', 'Detects the possible usage of a variable before the declaration is stepped over (either because it is later declared, or declared in another scope).','Move all variable declarations prior to any usage of the variable, and ensure that reaching a variable declaration does not depend on some conditional if it is used unconditionally.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (53,'void-constructor', 'Low', 'Detect the call to a constructor that is not implemented','Remove the constructor call.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (54,'calls-inside-a-loop', 'Low', 'Calls inside a loop might lead to a denial-of-service attack.','Favor pull over push strategy for external calls.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (55,'missing-events-access-control', 'Low', 'Detect missing events for critical access control parameters','Emit an event for critical parameter changes.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (56,'missing-events-arithmetic', 'Low', 'Detect missing events for critical arithmetic parameters.','Emit an event for critical parameter changes.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (57,'dangerous-unary-expressions', 'Low', 'Unary expressions such as x=+1 probably typos.','Remove the unary expression.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (58,'missing-zero-address-validation', 'Low', 'Detect missing zero address validation.','Check that the address is not zero.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (59,'reentrancy-vulnerabilities-2', 'Low', 'Detection of the reentrancy bug. Only report reentrancy that acts as a double call (see reentrancy-eth, reentrancy-no-eth).','Apply the check-effects-interactions pattern.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (60,'reentrancy-vulnerabilities-3', 'Low', 'Detects reentrancies that allow manipulation of the order or value of events.','Apply the check-effects-interactions pattern.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (61,'block-timestamp', 'Low', 'Dangerous usage of block.timestamp. block.timestamp can be manipulated by miners.','Avoid relying on block.timestamp.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (62,'assembly-usage', 'Informational', 'The use of assembly is error-prone and should be avoided.','Do not use evm assembly.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (63,'assert-state-change', 'Informational', 'Incorrect use of assert(). See Solidity best practices.','Use require for invariants modifying the state.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (64,'boolean-equality', 'Informational', 'Detects the comparison to boolean constants.','Remove the equality to the boolean constant.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (65,'cyclomatic-complexity', 'Informational', 'Detects functions with high (> 11) cyclomatic complexity.','Reduce cyclomatic complexity by splitting the function into several smaller subroutines.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (66,'deprecated-standards', 'Informational', 'Detect the usage of deprecated standards.','Replace all uses of deprecated symbols.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (67,'unindexed-erc20-event-parameters', 'Informational', 'Detects whether events defined by the ERC20 specification that should have some parameters as indexed are missing the indexed keyword.','Add the indexed keyword to event parameters that should include it, according to the ERC20 specification.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (68,'function-initializing-state', 'Informational', 'Detects the immediate initialization of state variables through function calls that are not pure/constant, or that use non-constant state variable.','Remove any initialization of state variables via non-constant state variables or function calls. If variables must be set upon contract deployment, locate initialization in the constructor instead.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (69,'incorrect-usage-of-using-for-statement', 'Informational', 'In Solidity, it is possible to use libraries for certain types, by the using-for statement (using <library> for <type>). However, the Solidity compiler doesnt check whether a given library has at least one function matching a given type. If it doesnt, such a statement has no effect and may be confusing.','Make sure that the libraries used in using-for statements have at least one function matching a type used in these statements.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (70,'low-level-calls', 'Informational', 'The use of low-level calls is error-prone. Low-level calls do not check for code existence or call success.','Avoid low-level calls. Check the call success. If the call is meant for a contract, check for code existence.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (71,'missing-inheritance', 'Informational', 'Detect missing inheritance.','Inherit from the missing interface or contract.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (72,'conformance-to-solidity-naming-conventions', 'Informational', 'Solidity defines a naming convention that should be followed. Rule exceptionsAllow constant variable name/symbol/decimals to be lowercase (RC20). Allow _ at the beginning of the mixed_case match for private variables and unused parameters.','Follow the Solidity naming convention.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (73,'different-pragma-directives-are-used', 'Informational', 'Detect whether different Solidity versions are used.','Use one Solidity version.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (74,'redundant-statements', 'Informational', 'Detect the usage of redundant statements that have no effect.','Remove redundant statements if they congest code but offer no value.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (75,'incorrect-versions-of-solidity', 'Informational', 'solc frequently releases new compiler versions. Using an old version prevents access to new Solidity security checks. We also recommend avoiding complex pragma statement.','Deploy with any of the following Solidity versions: 0.8.18 The recommendations take into account: Risks related to recent releases Risks of complex code generation changes Risks of new language features Risks of known bugsUse a simple pragma version that allows any of these versions. Consider using the latest version of Solidity for testing.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (76,'unimplemented-functions', 'Informational', 'Detect functions that are not implemented on derived-most contracts.','Implement all unimplemented functions in any contract you intend to use directly (not simply inherit from).');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (77,'unused-state-variable', 'Informational', 'Unused state variable.','Remove unused state variables.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (78,'costly-operations-inside-a-loop', 'Informational', 'Costly operations inside a loop might waste gas, so optimizations are justified.','Use a local variable to hold the loop computation result.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (79,'dead-code', 'Informational', 'Functions that are not sued.','Remove unused functions.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (80,'reentrancy-vulnerabilities-4', 'Informational', 'Detection of the reentrancy bug. Only report reentrancy that is based on transfer or send.','Apply the check-effects-interactions pattern.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (81,'variable-names-too-similar', 'Informational', 'Detect variables with names that are too similar.','Prevent variables from having similar names.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (82,'too-many-digits', 'Informational', 'Literals with many digits are difficult to read and review.','Use: Ether suffix, Time suffix, or The scientific notation');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (83,'cache-array-length', 'Optimization', 'Detects for loops that use length member of some storage array in their loop condition and dont modify it.','Cache the lengths of storage arrays if they are used and not modified in for loops.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (84,'state-variables-that-could-be-declared-constant', 'Optimization', 'State variables that are not updated following deployment should be declared constant to save gas.','Add the constant attribute to state variables that never change.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (85,'public-function-that-could-be-declared-external', 'Optimization', 'public functions that are never called by the contract should be declared external, and its immutable parameters should be located in calldata to save gas.','Use the external attribute for functions never called from the contract, and change the location of immutable parameters to calldata to save gas.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (86,'state-variables-that-could-be-declared-immutable', 'Optimization', 'State variables that are not updated following deployment should be declared immutable to save gas.','Add the immutable attribute to state variables that never change or are set only in the constructor.');"
                              "INSERT INTO Vulnerabilities (vulnerability_id, vulnerability_name, impact, description,recomendations) VALUES (87,'public-variable-read-in-external-context', 'Optimization', 'The contract reads its own variable using this, adding overhead of an unnecessary STATICCALL.','Read the variable directly from storage instead of calling the contract.');"
    }
    return valnrabilatieStatements