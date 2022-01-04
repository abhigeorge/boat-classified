from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Boat(models.Model):

    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for r in range(1950, (datetime.now().year+1)):
        year_choice.append((r,r))
    
    covers_choices = (
        ('Bimini Top', 'Bimini Top'),
        ('Spray hood', 'Spray hood'),
    )

    electrical_equipment_choices = (
        ('Shore power inlet', 'Shore power inlet'),
        ('Generator', 'Generator'),
        ('Inverter', 'Inverter'),
    )

    electronics_choices = (
        ('Depthsounder', 'Depthsounder'),
        ('Radar', 'Radar'),
        ('Log-speedometer', 'Log-speedometer'),
        ('Wind speed and direction', 'Wind speed and direction'),
        ('Repeater(s)', 'Repeater(s)'),
        ('TV set', 'TV set'),
        ('Navigation center', 'Navigation center'),
    )

    inside_equipment_choices = (
        ('Stern thruster', 'Stern thruster'),
        ('Dishwasher', 'Dishwasher'),
        ('Bow thruster', 'Bow thruster'),
        ('Electric bilge pump', 'Electric bilge pump'),
        ('Oven', 'Oven'),
        ('Manual bilge pump', 'Manual bilge pump'),
        ('Air compressor', 'Air compressor'),
    )

    outside_equipment_choices = (
        ('Teak cockpit', 'Teak cockpit'),
        ('Cockpit shower', 'Cockpit shower'),
        ('Teak sidedecks', 'Teak sidedecks'),
        ('Hydraulic gangway', 'Hydraulic gangway'),
        ('Radar reflector', 'Radar reflector'),
        ('Tender', 'Tender'),
        ('Cockpit cushions', 'Cockpit cushions'),
    )

    rigging_choices = (
        ('Steering wheel', 'Steering wheel'),
        ('Electric winch', 'Electric winch'),
    )

    sails_choices = (
        ('Fully battened mainsail', 'Fully battened mainsail'),
        ('Gennaker/Cruising spinnaker', 'Gennaker/Cruising spinnaker'),
        ('Furling genoa', 'Furling genoa'),
    )


    boat_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    boat_type = models.CharField(max_length=100)
    boat_class = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    hull_material = models.CharField(max_length=100)
    boat_location = models.CharField(max_length=100)
    tax_status = models.CharField(max_length=100)
    loa = models.CharField(max_length=100)
    beam = models.CharField(max_length=100)
    max_draft = models.CharField(max_length=100)
    min_draft = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)
    engine_make = models.CharField(max_length=100)
    engine_model = models.CharField(max_length=100)
    engine_year = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    drive_type = models.CharField(max_length=100)
    propeller_type = models.CharField(max_length=100)
    folding_propeller = models.CharField(max_length=100)
    engine_usage_hours = models.IntegerField()
    certification = models.CharField(max_length=100)
    cabins = models.IntegerField()
    double_berths = models.IntegerField()
    heads = models.IntegerField()
    fuel_tanks = models.IntegerField()
    fresh_water_tanks = models.IntegerField()
    windlass = models.CharField(max_length=100)
    boat_description = RichTextField()
    covers = MultiSelectField(choices=covers_choices, null=True)
    electrical_equipment = MultiSelectField(choices=electrical_equipment_choices, null=True)
    electronics = MultiSelectField(choices=electronics_choices, null=True)
    inside_equipment = MultiSelectField(choices=inside_equipment_choices, null=True)
    outside_equipment = MultiSelectField(choices=outside_equipment_choices, null=True)
    rigging = MultiSelectField(choices=rigging_choices, null=True)
    sails = MultiSelectField(choices=sails_choices, null=True)
    boat_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    boat_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    boat_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    boat_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    boat_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

def __str__(self):
        return self.boat_title



