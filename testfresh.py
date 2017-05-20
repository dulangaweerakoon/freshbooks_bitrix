import freshbooks

  
# get data
freshbooks.setup('cwbsolutionspteltd.freshbooks.com', '08bf24f443a1882de4f109d791209c3a', user_agent_name='cwbsolutionspteltd')
clients = freshbooks.Client.list()
# client_names = [clients.first_name]
print 'Name','\t\t','Organization';
for client in clients:
    print client.first_name,client.last_name,'\t\t',client.organization;
#print clients[0].first_name
# client_1 = freshbooks.Client.get(<client_id>)
    
# # update data
# changed_client = freshbooks.Client()
# changed_client.client_id = client_1.client_id
# changed_client.first_name = u'Jane'
# r = freshbooks.call_api('client.update', changed_client)
# assert(r.success)