# Category Routing for PDP Image Master

Use this reference before applying category-specific rules. The purpose is to classify the product from images and evidence, not from a fixed assumption.

## Routing Principle

Classify by the product's buyer use case and proof requirements, not only by its visual appearance.

Look at:

- Product shape, materials, labels, parts, packaging, and visible use context
- Folder/file names, SKU names, spreadsheet fields, and product titles
- Props in the image, but do not assume props are included in the package
- User instructions, benchmark references, and brand rules
- Safety-sensitive contact: food, beverage, skin, baby, pet, electronics, heat, water, body contact

## Multi-Category Products

If a product fits multiple references, apply all relevant references and use the strictest claim rules.

Examples:

- Electric makeup brush cleaner: beauty + electronics
- Heated pet bowl: pet + electronics + food-contact
- Insulated travel bottle: beverage-contact + outdoor
- LED vanity mirror: beauty + electronics + home
- Jewelry gift box: jewelry/gifts + home/decor packaging

## Category References

### Beverage-contact / barware / drinkware

Use `category-beverage-contact.md` when the product touches beverages or is used with drinking, pouring, storing, chilling, decanting, or serving drinks.

Typical signs:

- Glasses, cups, mugs, bottles, decanters, wine/whiskey accessories, bottle openers, ice molds, straws, drink dispensers
- Visible liquids, bar counter, wine/whiskey bottle, coffee/tea context
- Claims may involve food-contact safety, capacity, seal, leakproof, heat/cold resistance, lead-free, BPA-free

### Apparel / wearable accessories

Use `category-apparel-accessories.md` when fit, styling, body relation, comfort, fabric, or daily wear matters.

Typical signs:

- Clothing, bags, hats, belts, gloves, scarves, shoes, socks, straps, wearable pouches
- Claims may involve material, fit, sizing, waterproofing, weight, capacity, wash care, comfort

### Beauty / personal care

Use `category-beauty-personal-care.md` when the product is used on skin, hair, nails, face, cosmetics, grooming, or personal hygiene.

Typical signs:

- Cosmetics packaging, applicators, skincare tools, hair tools, nail tools, mirrors, razors, grooming tools, massagers
- Claims may involve skin/hair outcomes, hypoallergenic, dermatologist-tested, ingredients, hygiene, before/after

### Electronics / appliances / lighting

Use `category-electronics-appliances.md` when the product has power, battery, charging, lights, sensors, display, motor, smart function, or heat.

Typical signs:

- Cable, plug, button, screen, LED, motor, charging port, appliance body, remote, app UI, battery icon
- Claims may involve battery life, voltage, wattage, waterproof rating, compatibility, safety certifications, performance

### Home / kitchen / storage / decor

Use `category-home-kitchen.md` when the product is used in a room, kitchen, desk, bathroom, storage area, or home organization context.

Typical signs:

- Furniture, decor, shelf, organizer, container, kitchen tool, bedding, bathroom item, cleaning tool
- Claims may involve dimensions, capacity, load-bearing, material, room fit, care, package contents

### Jewelry / keepsakes / premium gifts

Use `category-jewelry-gifts.md` when the product is small, ornamental, sentimental, personalized, premium gift-oriented, or worn as jewelry.

Typical signs:

- Rings, necklaces, bracelets, pendants, watches, keepsake boxes, engraved items, gift packaging
- Claims may involve material, plating, gemstone, hypoallergenic, personalization, gift occasion, size/fit

### Tools / outdoor / auto / sports / pet

Use `category-tools-outdoor-pet.md` when the product is used for repair, utility, outdoor conditions, vehicles, sports, pets, durability, or active use.

Typical signs:

- Tools, hardware, camping items, car accessories, bike accessories, sports gear, pet bowls/toys/harnesses, leashes
- Claims may involve durability, load, weather resistance, pet safety, vehicle compatibility, measurements, materials

## If No Category Reference Fits

Use universal PDP rules:

1. Identify the main buying uncertainty.
2. Build a sequence that answers desire, use, proof, scale/fit, and specs.
3. Keep unsupported claims out of image text.
4. Use visual style based on product price, scene, brand, and benchmark references.
5. Add a short `category_notes` section in `pdp_plan.md` explaining how the category was inferred.
