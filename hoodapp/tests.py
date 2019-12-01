from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestNeighbourhoodModel(TestCase):
  '''
  test class for  the neighbour model
  '''
  def setUp(self):
    '''
    the startup class of the class
    '''
    self.new_user = User(username = 'Liz')
    self.new_user.save()
    self.new_neighbourhood = Neighborhood(name = 'Ayany-court',location = 'KIbera',occupants = '22', image='hood.jpg', datecreated = '2019-10-30', health_department_contact='0700112233',police_authority_contact='0790234565',user = self.new_user)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_neighbourhood,Neighborhood))

  def test_create_neighbourhood(self):
    self.new_neighbourhood.save_neighborhood()
    neighborhoods = Neighborhood.objects.all()
    self.assertTrue(len(neighborhoods) > 0)


  def test_delete_neighbourhood(self):
    self.new_neighbourhood.save_neighborhood()
    self.new_neighbourhood.delete_neighborhood()
    neighborhoods = Neighborhood.objects.all()
    self.assertEqual(len(neighborhoods),0)


class TestBusinessModels(TestCase):
  '''
  test classs that test the business model and its functions
  '''
  def setUp(self):
    '''
    the functions that runs at the begin of the test
    '''
    self.new_user = User(username = 'Sharly')
    self.new_user.save()
    self.new_neighborhood = Neighborhood(name = 'Ayany-court',location = 'KIbera',occupants = '22', image='hood.jpg', datecreated = '2019-10-30', health_department_contact='0700112233',police_authority_contact='0790234565',user = self.new_user)
    self.new_neighborhood.save()
    self.new_business = Business(name = 'mama mboga',email= 'mboga@gmail.com', user=self.new_user, neighborhood=self.new_neighborhood )

  def test_business_instance(self):
    self.assertTrue(isinstance(self.new_business,Business))

  def test_create_a_business(self):
    self.new_business.save_business()
    business = Business.objects.all()
    self.assertTrue(len(business) > 0)

  def test_delete_a_business(self):
    self.new_business.save_business()
    self.new_business.delete_business()
    business = Business.objects.all()
    self.assertEqual(len(business),0)

  def test_search_neighbourhood_by_name(self):
    self.new_user = User(username = 'Mercy')
    self.new_user.save()
    self.new_business = Business(name = 'mama mboga',email= 'mboga@gmail.com', user=self.new_user, neighborhood=self.new_neighborhood )
    self.new_business.save_business()
    search_result = Business.search_by_name('mama mboga')
    self.assertEqual(len(search_result),1)





class TestPostModels(TestCase):
    '''
    test classs that test the business model and its functions
    '''

    def setUp(self):
       '''
       the functions that runs at the begin of the test
       '''
       self.new_user = User(username = 'Jane')
       self.new_user.save()
       self.new_neighborhood = Neighborhood(name = 'Ayany-court',location = 'KIbera',occupants = '22', image='hood.jpg', datecreated = '2019-10-30', health_department_contact='0700112233',police_authority_contact='0790234565',user = self.new_user)
       self.new_neighborhood.save()
       self.new_post = Post(title = 'mama',story= 'mboga@gmail.com', user=self.new_user, neighborhood=self.new_neighborhood )
       self.new_post.save()
       self.new_business = Business(name = 'mama mboga',email= 'mboga@gmail.com', user=self.new_user, neighborhood=self.new_neighborhood )
       self.new_business.save()


    def test_post_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))


    def test_create_a_post(self):
      self.new_post.save_post()
      posts = Post.objects.all()
      self.assertTrue(len(posts) > 0)

    def test_delete_a_post(self):
      self.new_post.save_post()
      self.new_post.delete_post()
      posts = Post.objects.all()
      self.assertEqual(len(posts),0)
