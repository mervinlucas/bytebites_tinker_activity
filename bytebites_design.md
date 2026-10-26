classDiagram
    class Customer {
        +str name
        +list purchase_history
        +add_purchase(order) None
        +has_purchase_history() bool
    }

    class MenuItem {
        +str name
        +float price
        +str category
        +float popularity_rating
    }

    class Menu {
        +list items
        +add_item(item) None
        +filter_by_category(category) list
    }

    class Order {
        +list items
        +add_item(item) None
        +calculate_total() float
    }

    Customer "1" --> "0..*" Order : purchase history
    Menu "1" o-- "0..*" MenuItem : contains
    Order "1" o-- "0..*" MenuItem : selected items
