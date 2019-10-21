class Cat:
    """
    Write Class Cat which will receive age from user
    * Add to class average_speed variable which will get it's values
      from private method _set_average_speed()

    * Add to class saturation_level variable with value 50

    * Implement private methods _increase_saturation_level and _reduce_saturation_level
      that will receive value and add/subtract from saturation_level this value
      if saturation_level is less than 0, return 0
      if saturation_level is grosser than 100, return 100

    * Implement method eat which will receive from user product value
      if product eq fodder use _increase_saturation_level with value eq 10
      if product eq apple use _increase_saturation_level with value eq 5
      if product eq milk use _increase_saturation_level with value eq 2

    * Implement private method _set_average_speed
      if age less or eq 7 return 12
      if age between 7(not including) and 10(including) return 9
      if age grosser than 10(not including) return 6

    * Implement method run it receives hours value
      Calculate run km per hours remember that you have average_speed value
      Than if your cat run less or eq than 25 _reduce_saturation_level with value 2
      if it runs between 25(not including) and 50(including) than _reduce_saturation_level with value 5
      if it runs between 50(not including) and 100(including) than _reduce_saturation_level with value 15
      if it runs between 100(not including) and 200(including) than _reduce_saturation_level with value 25
      if it runs more than 200(not including) than _reduce_saturation_level with value 50

      return text like this: f"Your cat ran {ran_km} kilometers"

    * Implement get_saturation_level and return saturation_level
      if saturation_level eq 0 return text like this: "Your cat is dead :("

    * Implement get_average_speed and return average_speed

    """

    saturation_level = 50

    def __init__(self, age):
        self.age = age

    def eat(self, product):
        if product == 'fodder':
            self._increase_saturation_level(10)
        elif product == 'apple':
            self._increase_saturation_level(5)
        elif product == 'milk':
            self._increase_saturation_level(2)
        return self.saturation_level

    def _reduce_saturation_level(self, value):
        self.saturation_level = self.saturation_level - value
        if self.saturation_level < 0:
            self.saturation_level = 0

    def _increase_saturation_level(self, value):
        self.saturation_level += value
        if self.saturation_level > 100:
            return 100
        return self.saturation_level

    def _set_average_speed(self,average_speed):
        if self.age <= 7:
            self.average_speed = 12
        elif self.age > 7 or self.age <= 10:
            self.average_speed = 9
        elif self.age > 10:
            self.average_speed = 6

    def run(self, hours):
        self.hours = self.average_speed * hours
        if self.hours <= 25:
            self.saturation_level = self.saturation_level - 2
        if self.hours > 25 or self.hours <= 50:
            self.saturation_level = self.saturation_level - 5
        if self.hours > 50 or self.hours <= 100:
            self.saturation_level = self.saturation_level - 15
        if self.hours > 100 or self.hours <= 200:
            self.saturation_level = self.saturation_level - 25
        if self.hours >= 200:
            self.saturation_level = self.saturation_level - 50
        return f"Your cat ran {self.hours} kilometers"

    def get_saturation_level(self):
        if self.saturation_level <= 0:
            return 'Your cat is dead :('
        return self.saturation_level

    def get_average_speed(self):
        return self.average_speed



class Cheetah(Cat):
    """
    * Inherit from class Cat

    * Redefine method eat from parent class it will receive product value
      if product eq gazelle use _increase_saturation_level from parent class with value 30
      if product eq rabbit use _increase_saturation_level from parent class with value 15

    * Redefine method _set_average_speed
      if age less or eq 5 return 90
      if age between 5 and 15(including) return 75
      if age grosser 15(not including) return 40
    """

    def eat(self, product):
        self.product = product
        if self.product == 'gazelle':
            self.saturation_level = self.saturation_level + 30
        if self.product == 'rabbit':
            self.saturation_level = self.saturation_level + 15
        return self.saturation_level

    def _set_average_speed(self,average_speed):
        self.average_speed = average_speed
        if self.age <= 5:
            self.average_speed = 90
        if self.age > 5 or self.age <= 15:
            self.average_speed = 75
        if self.age > 15:
            self.average_speed = 40
        return self.average_speed


class Wall:
    """
    * Implement class Wall which receives such parameters: width and height

    * Implement method wall_square which return result of simple square formula of rectangle

    * Implement method number_of_rolls_of_wallpaper which receives such parameters: roll_width_m, roll_length_m
      (_m in the parameters name means meters) return number of rolls of wallpaper

      Example:
          count of lines in roll eq roll length in meters divide height of the wall (use rounding down)
          count of lines eq width of the wall divide roll width in meters
          number of rolls of wallpaper eq count of lines divide  count of lines in roll
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wall_square(self):
        return self.width * self.height

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        self.roll_width_m = roll_width_m
        self.roll_length_m = roll_length_m
        count_of_lines_in_roll = self.roll_length_m/self.height
        count_of_lines = self.width/self.roll_width_m
        number_of_rolls = count_of_lines/count_of_lines_in_roll
        return number_of_rolls


class Roof:
    """
        * Implement class Roof which receives such parameters: width, height and roof_type

        * Implement method roof_square that returns square of the roof
          if roof_type eq "gable" the roof square if simple rectangle square formula multiplied 2
          if roof_type eq "single-pitch" the roof square if simple rectangle square formula
          if other roof_type raise ValueError like this "Sorry there is only two types of roofs"

    """

    def __init__(self, width, height, roof_type):
        self.width = width
        self.height = height
        self.roof_type = roof_type

    def roof_square(self):
        if self.roof_type == 'gable':
            self.roof_square = (self.width * self.height) * 2
        if self.roof_type == 'single-pitch':
            self.roof_square = self.width * self.height
        else:
            raise ValueError ("Sorry there is only two types of roofs")
        return self.roof_square


class Window:
    """
       * Implement class Window which receives such parameters: width and height

       * Implement method window_square which return result of simple square formula of rectangle

    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def window_square(self):
        return self.width * self.height


class Door:
    """
     * Implement class Door which receives such parameters: width and height
      add variables wood_price eq 10, metal_price eq 3

     * Implement method door_square which return result of simple square formula of rectangle

     * Implement method door_square which receives material value as a parameter
       if material eq wood return door_square multiplied on wood_price
       if material eq metal return door_square multiplied on metal_price
       if material value is another one (not metal or wood) raise ValueError "Sorry we don't have such material"

     *  Implement method update_wood_price which receives new_price value and updates your old price

     *  Implement method update_metal_price which receives new_price value and updates your old price

    """

    wood_price = 10
    metal_price = 3

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def door_square(self):
        self.door_square = self.width * self.height
        return self.door_square

    def door_price(self, material):
        self.material = material
        if self.material == 'wood':
            self.door_price = self.door_square * self.wood_price
        if self.material == 'metal':
            self.door_price = self.door_square * self.metal_price
        else:
            raise ValueError("Sorry we don't have such material")
        return self.door_price

    def update_wood_price(self, new_price):
        self.wood_price = new_price

    def update_metal_price(self,new_price):
        self.metal_price = new_price


class House(Wall, Roof, Window, Door):
    """
    !!!! DON'T WRITE NEW METHODS TO THIS CLASS EXCEPT FOR THOSE LISTED BELOW !!!

    * Add super private variable __walls and its value will be empty list
    * Add super private variable __windows and its value will be empty list
    * Add super private variable __roof and its value will be None
    * Add super private variable __door and its value will be None

    * Implement method create_wall which will create new wall using class Wall and add it to the __walls list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      if user have more than 4 walls raise ValueError "Our house can not have more than 4 walls"

    * Implement method create_roof which will create new roof using class Roof and assign it to the __roof variable
      it receives parameters width, height and roof_type
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another roof if we already have another one,
              otherwise raise ValueError "The house can not have two roofs"

    * Implement method create_window which will create new window using class Window and add it to the __windows list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"

    * Implement method create_door which will create new door using class Door and assign it to the __door variable
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another door if we already have another one,
              otherwise raise ValueError "The house can not have two doors"

    * Implement method get_count_of_walls that returns count of walls

    * Implement method get_count_of_windows that returns count of windows

    * Implement method get_door_price that receives material value and returns price of the door

    * Implement method update_wood_price that receives new_wood_price and updates old one

    * Implement method update_metal_price that receives new_metal_price and updates old one

    * Implement method get_roof_square that returns the roof square

    * Implement method get_walls_square that returns sum of all walls square that we have

    * Implement method get_windows_square that returns sum of all windows square that we have

    * Implement method get_door_square that returns the square of the door

    * Implement method get_number_of_rolls_of_wallpapers that returns sum of the number of rolls of wallpapers
      needed for all our walls
      it receives roll_width_m, roll_length_m parameters
      Check if roll_width_m or roll_length_m eq 0 raise ValueError "Sorry length must be not 0"

    * Implement method get_room_square that returns the square of our room
      (from walls_square divide windows and door square)

    """

    def __init__(self):
        super().__init__(self, 'Wall', [])
        super().__init__(self, 'Roof', [])
        super().__init__(self, 'Window', None)
        super().__init__(self, 'Door', None)

    def create_wall(self, width, height):

        pass

    def create_roof(self):
        pass

    def create_window(self):
        pass

    def create_door(self):
        pass

    def get_count_of_walls(self):
        pass

    def get_count_of_windows(self):
        pass

    def get_door_price(self):
        pass

    def update_wood_price(self):
        pass

    def update_metal_price(self):
        pass

    def get_roof_square(self):
        pass

    def get_walls_square(self):
        pass

    def get_windows_square(self):
        pass

    def get_door_square(self):
        pass

    def get_number_of_rolls_of_wallpapers(self):
        pass

    def get_room_square(self):
        pass
