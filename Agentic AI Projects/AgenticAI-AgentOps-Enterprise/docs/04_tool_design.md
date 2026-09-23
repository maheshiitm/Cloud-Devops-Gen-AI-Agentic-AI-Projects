# Tool Design

Every tool has a narrow purpose, typed contract, permissions and a mutating flag. Recommended lifecycle: validate -> authorize -> execute -> audit -> return structured result.