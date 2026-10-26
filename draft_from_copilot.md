┌────────────────────────────────┐             ┌────────────────────────────────┐
│            Customer            │             │             Order              │
├────────────────────────────────┤             ├────────────────────────────────┤
│ - name: str                    │ 1      0..* │ - items: list[MenuItem]        │
│ - purchase_history: list[Order]│◇───────────▶│                                │
├────────────────────────────────┤   places    ├────────────────────────────────┤
│ + add_order(order: Order)      │             │ + add_item(item: MenuItem)     │
│ + is_verified() -> bool        │             │ + calculate_total() -> float   │
└────────────────────────────────┘             └───────────────┬────────────────┘
                                                               │ contains
                                                               │ 0..*
┌────────────────────────────────┐             ┌───────────────▼────────────────┐
│              Menu              │             │            MenuItem            │
├────────────────────────────────┤             ├────────────────────────────────┤
│ - items: list[MenuItem]        │ 1      0..* │ - name: str                    │
│                                │◇───────────▶│ - price: float                 │
├────────────────────────────────┤    holds    │ - category: str                │
│ + filter_by_category(          │             │ - popularity_rating: float     │
│     category: str)             │             ├────────────────────────────────┤
│     -> list[MenuItem]          │             │ (data only: no methods         │
│                                │             │  needed beyond __init__)       │
└────────────────────────────────┘             └────────────────────────────────┘
