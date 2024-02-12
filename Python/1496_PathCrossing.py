def isPathCrossing(path):
        """
        :type path: str
        :rtype: bool
        """
        
        current_x = 0
        current_y = 0
        positions = [(0,0)]
        
        for i in range(len(path)):
            if (path[i]=="N"):
                current_y += 1
            if (path[i]=="S"):
                current_y -= 1
            if (path[i]=="E"):
                current_x += 1
            if (path[i]=="W"):
                current_x -= 1
            
            current_position = (current_x, current_y)
            if (positions.count(current_position)!=0):
                return True 
            
            positions.append(current_position)
        return False 

if __name__ == "__main__":
    print(isPathCrossing("NES"))
    print(isPathCrossing("NESWW"))
        
        
        
        