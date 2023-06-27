// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package airflow

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides an Airflow user.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/Hellthrashers/pulumi-airflow/sdk/go/airflow"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := airflow.NewUser(ctx, "example", &airflow.UserArgs{
//				Email:     pulumi.String("example"),
//				FirstName: pulumi.String("example"),
//				LastName:  pulumi.String("example"),
//				Username:  pulumi.String("example"),
//				Password:  pulumi.String("example"),
//				Roles: pulumi.StringArray{
//					pulumi.Any(airflow_role.Example.Name),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Users can be imported using the user key. terraform
//
// ```sh
//
//	$ pulumi import airflow:index/user:User example example
//
// ```
type User struct {
	pulumi.CustomResourceState

	// Whether the user is active.
	Active pulumi.BoolOutput `pulumi:"active"`
	// The user's email
	Email pulumi.StringOutput `pulumi:"email"`
	// The number of times the login failed.
	FailedLoginCount pulumi.IntOutput `pulumi:"failedLoginCount"`
	// The user firstname
	FirstName pulumi.StringOutput `pulumi:"firstName"`
	// The user lastname
	LastName pulumi.StringOutput `pulumi:"lastName"`
	// The login count.
	LoginCount pulumi.StringOutput `pulumi:"loginCount"`
	// The user password.
	Password pulumi.StringOutput `pulumi:"password"`
	// A set of User roles to attach to the User.
	Roles pulumi.StringArrayOutput `pulumi:"roles"`
	// The username
	Username pulumi.StringOutput `pulumi:"username"`
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOption) (*User, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Email == nil {
		return nil, errors.New("invalid value for required argument 'Email'")
	}
	if args.FirstName == nil {
		return nil, errors.New("invalid value for required argument 'FirstName'")
	}
	if args.LastName == nil {
		return nil, errors.New("invalid value for required argument 'LastName'")
	}
	if args.Password == nil {
		return nil, errors.New("invalid value for required argument 'Password'")
	}
	if args.Roles == nil {
		return nil, errors.New("invalid value for required argument 'Roles'")
	}
	if args.Username == nil {
		return nil, errors.New("invalid value for required argument 'Username'")
	}
	var resource User
	err := ctx.RegisterResource("airflow:index/user:User", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUser gets an existing User resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserState, opts ...pulumi.ResourceOption) (*User, error) {
	var resource User
	err := ctx.ReadResource("airflow:index/user:User", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering User resources.
type userState struct {
	// Whether the user is active.
	Active *bool `pulumi:"active"`
	// The user's email
	Email *string `pulumi:"email"`
	// The number of times the login failed.
	FailedLoginCount *int `pulumi:"failedLoginCount"`
	// The user firstname
	FirstName *string `pulumi:"firstName"`
	// The user lastname
	LastName *string `pulumi:"lastName"`
	// The login count.
	LoginCount *string `pulumi:"loginCount"`
	// The user password.
	Password *string `pulumi:"password"`
	// A set of User roles to attach to the User.
	Roles []string `pulumi:"roles"`
	// The username
	Username *string `pulumi:"username"`
}

type UserState struct {
	// Whether the user is active.
	Active pulumi.BoolPtrInput
	// The user's email
	Email pulumi.StringPtrInput
	// The number of times the login failed.
	FailedLoginCount pulumi.IntPtrInput
	// The user firstname
	FirstName pulumi.StringPtrInput
	// The user lastname
	LastName pulumi.StringPtrInput
	// The login count.
	LoginCount pulumi.StringPtrInput
	// The user password.
	Password pulumi.StringPtrInput
	// A set of User roles to attach to the User.
	Roles pulumi.StringArrayInput
	// The username
	Username pulumi.StringPtrInput
}

func (UserState) ElementType() reflect.Type {
	return reflect.TypeOf((*userState)(nil)).Elem()
}

type userArgs struct {
	// The user's email
	Email string `pulumi:"email"`
	// The user firstname
	FirstName string `pulumi:"firstName"`
	// The user lastname
	LastName string `pulumi:"lastName"`
	// The user password.
	Password string `pulumi:"password"`
	// A set of User roles to attach to the User.
	Roles []string `pulumi:"roles"`
	// The username
	Username string `pulumi:"username"`
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// The user's email
	Email pulumi.StringInput
	// The user firstname
	FirstName pulumi.StringInput
	// The user lastname
	LastName pulumi.StringInput
	// The user password.
	Password pulumi.StringInput
	// A set of User roles to attach to the User.
	Roles pulumi.StringArrayInput
	// The username
	Username pulumi.StringInput
}

func (UserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userArgs)(nil)).Elem()
}

type UserInput interface {
	pulumi.Input

	ToUserOutput() UserOutput
	ToUserOutputWithContext(ctx context.Context) UserOutput
}

func (*User) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (i *User) ToUserOutput() UserOutput {
	return i.ToUserOutputWithContext(context.Background())
}

func (i *User) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserOutput)
}

// UserArrayInput is an input type that accepts UserArray and UserArrayOutput values.
// You can construct a concrete instance of `UserArrayInput` via:
//
//	UserArray{ UserArgs{...} }
type UserArrayInput interface {
	pulumi.Input

	ToUserArrayOutput() UserArrayOutput
	ToUserArrayOutputWithContext(context.Context) UserArrayOutput
}

type UserArray []UserInput

func (UserArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*User)(nil)).Elem()
}

func (i UserArray) ToUserArrayOutput() UserArrayOutput {
	return i.ToUserArrayOutputWithContext(context.Background())
}

func (i UserArray) ToUserArrayOutputWithContext(ctx context.Context) UserArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserArrayOutput)
}

// UserMapInput is an input type that accepts UserMap and UserMapOutput values.
// You can construct a concrete instance of `UserMapInput` via:
//
//	UserMap{ "key": UserArgs{...} }
type UserMapInput interface {
	pulumi.Input

	ToUserMapOutput() UserMapOutput
	ToUserMapOutputWithContext(context.Context) UserMapOutput
}

type UserMap map[string]UserInput

func (UserMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*User)(nil)).Elem()
}

func (i UserMap) ToUserMapOutput() UserMapOutput {
	return i.ToUserMapOutputWithContext(context.Background())
}

func (i UserMap) ToUserMapOutputWithContext(ctx context.Context) UserMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserMapOutput)
}

type UserOutput struct{ *pulumi.OutputState }

func (UserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (o UserOutput) ToUserOutput() UserOutput {
	return o
}

func (o UserOutput) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return o
}

// Whether the user is active.
func (o UserOutput) Active() pulumi.BoolOutput {
	return o.ApplyT(func(v *User) pulumi.BoolOutput { return v.Active }).(pulumi.BoolOutput)
}

// The user's email
func (o UserOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.Email }).(pulumi.StringOutput)
}

// The number of times the login failed.
func (o UserOutput) FailedLoginCount() pulumi.IntOutput {
	return o.ApplyT(func(v *User) pulumi.IntOutput { return v.FailedLoginCount }).(pulumi.IntOutput)
}

// The user firstname
func (o UserOutput) FirstName() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.FirstName }).(pulumi.StringOutput)
}

// The user lastname
func (o UserOutput) LastName() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.LastName }).(pulumi.StringOutput)
}

// The login count.
func (o UserOutput) LoginCount() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.LoginCount }).(pulumi.StringOutput)
}

// The user password.
func (o UserOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.Password }).(pulumi.StringOutput)
}

// A set of User roles to attach to the User.
func (o UserOutput) Roles() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *User) pulumi.StringArrayOutput { return v.Roles }).(pulumi.StringArrayOutput)
}

// The username
func (o UserOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.Username }).(pulumi.StringOutput)
}

type UserArrayOutput struct{ *pulumi.OutputState }

func (UserArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*User)(nil)).Elem()
}

func (o UserArrayOutput) ToUserArrayOutput() UserArrayOutput {
	return o
}

func (o UserArrayOutput) ToUserArrayOutputWithContext(ctx context.Context) UserArrayOutput {
	return o
}

func (o UserArrayOutput) Index(i pulumi.IntInput) UserOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *User {
		return vs[0].([]*User)[vs[1].(int)]
	}).(UserOutput)
}

type UserMapOutput struct{ *pulumi.OutputState }

func (UserMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*User)(nil)).Elem()
}

func (o UserMapOutput) ToUserMapOutput() UserMapOutput {
	return o
}

func (o UserMapOutput) ToUserMapOutputWithContext(ctx context.Context) UserMapOutput {
	return o
}

func (o UserMapOutput) MapIndex(k pulumi.StringInput) UserOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *User {
		return vs[0].(map[string]*User)[vs[1].(string)]
	}).(UserOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserInput)(nil)).Elem(), &User{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserArrayInput)(nil)).Elem(), UserArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserMapInput)(nil)).Elem(), UserMap{})
	pulumi.RegisterOutputType(UserOutput{})
	pulumi.RegisterOutputType(UserArrayOutput{})
	pulumi.RegisterOutputType(UserMapOutput{})
}